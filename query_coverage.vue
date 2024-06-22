<template>
    <div>
      <h2>Coverage Data</h2>
      <ul v-if="coverageData.length > 0">
        <li v-for="(coverage, index) in coverageData" :key="index">
          <h3>Class Name: {{ coverage.className }}</h3>
          <p>Class Code: {{ coverage.classCode }}</p>
          <p>Dependent: {{ coverage.dependent }}</p>
          <p v-if="coverage.principal">Principal: {{ coverage.principal }}</p>
          <h4>Payors:</h4>
          <ul>
            <li v-for="(payor, idx) in coverage.payors" :key="idx">
              <p>Display: {{ payor.display }}</p>
              <p>Reference: {{ payor.reference }}</p>
            </li>
          </ul>
          <h4>Related Persons:</h4>
          <ul v-if="coverage.relatedPersons.length > 0">
            <li v-for="(person, idx) in coverage.relatedPersons" :key="idx">
              <h5>{{ person.role }}</h5>
              <p>Firstname: {{ person.firstname }}</p>
              <p>Lastname: {{ person.lastname }}</p>
              <p>DOB: {{ person.dob }}</p>
              <p>Gender: {{ person.gender }}</p>
            </li>
          </ul>
        </li>
      </ul>
      <p v-else>No coverage data available.</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        coverageData: [],
        apiBaseUrl: 'your_api_base_url_here',
        identifier: 'your_identifier_here'
      };
    },
    mounted() {
      this.fetchCoverageData();
    },
    methods: {
      async fetchCoverageData() {
        try {
          const response = await axios.get(`${this.apiBaseUrl}/Coverage?identifier=${this.identifier}`);
          const coverages = response.data.entry.map(entry => entry.resource);
          const coverageDataPromises = coverages.map(coverage => {
            const classCode = coverage.class[0].value || '';
            const className = coverage.class[0].name || '';
            const dependent = coverage.dependent || '';
            const principalRef = coverage.subscriber.reference || '';
  
            const payors = coverage.payor.map(payor => ({
              display: payor.display || '',
              reference: payor.reference || ''
            }));
  
            // Fetch principal details if available
            let principalDetailsPromise = Promise.resolve(null);
            if (principalRef) {
              const principalId = principalRef.split('/')[1];
              principalDetailsPromise = this.fetchPatient(principalId);
            }
  
            const relatedPersonsPromises = payors.map(payor => {
              if (payor.display === 'Spouse' || payor.display.startsWith('Child')) {
                const personId = payor.reference.split('/')[1];
                return this.fetchRelatedPerson(personId, payor.display);
              }
              return Promise.resolve(null);
            });
  
            return Promise.all([principalDetailsPromise, ...relatedPersonsPromises]).then(([principalDetails, ...relatedPersons]) => {
              const principal = principalDetails ? {
                firstname: principalDetails.name[0].given[0] || '',
                lastname: principalDetails.name[0].family || '',
                dob: principalDetails.birthDate || '',
                gender: principalDetails.gender || ''
              } : null;
  
              return {
                className,
                classCode,
                dependent,
                principal,
                payors,
                relatedPersons: relatedPersons.filter(person => person !== null)
              };
            });
          });
  
          Promise.all(coverageDataPromises).then(coverageData => {
            this.coverageData = coverageData;
          }).catch(error => {
            console.error('Error fetching coverage data:', error);
          });
  
        } catch (error) {
          console.error('Error fetching coverage data:', error);
        }
      },
      async fetchPatient(patientId) {
        try {
          const response = await axios.get(`${this.apiBaseUrl}/Patient/${patientId}`);
          return response.data;
        } catch (error) {
          console.error(`Error fetching patient details with ID ${patientId}:`, error);
          return null;
        }
      },
      async fetchRelatedPerson(personId, role) {
        try {
          const response = await axios.get(`${this.apiBaseUrl}/RelatedPerson/${personId}`);
          const relatedPerson = response.data;
          return {
            role,
            firstname: relatedPerson.name[0].given[0] || '',
            lastname: relatedPerson.name[0].family || '',
            dob: relatedPerson.birthDate || '',
            gender: relatedPerson.gender || ''
          };
        } catch (error) {
          console.error(`Error fetching ${role} details with ID ${personId}:`, error);
          return null;
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add your component-specific styles here */
  </style>
  