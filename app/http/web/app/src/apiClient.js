import axios from 'axios';

const BASE_URI = 'http://localhost:4433';

const client = axios.create({
 baseURL: BASE_URI,
 json: true
});

class APIClient {
 constructor(accessToken) {
   this.accessToken = accessToken;
 }

 createKudo (repo) {
   return this.http('post', '/kudos', repo);
 }

 deleteKudo (repo) {
   return this.http('delete', `/kudos/${repo.id}`);
 }

 getKudos () {
   return this.http('get', '/kudos');
 }

 async http (method, resource, data) {
   return client({
     method,
     url: resource,
     data,
     headers: {
       Authorization: `Bearer ${this.accessToken}`
     }
   }).then(resp => {
     return resp.data ? resp.data : [];
   })
 }
}

export default APIClient;