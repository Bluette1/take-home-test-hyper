import http from "../http-common";

class AuthService {
  register() {
    return http.post("/auth/signup");
  }

  login(data) {
    return http.post("/auth/signin", data);
    // set access token in local storage
    // set redux store property: logged in
  }

  logout(data) {
    // remove access token in local storage
    // set redux store property: logged in to false

  }
}

export default new AuthService();