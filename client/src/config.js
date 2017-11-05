/*
 * Config
 */

const API_BASE = 'http://localhost:8000'
const LOGIN_URL = `${API_BASE}/rest-auth/login/`
const VERIFY_URL = `${API_BASE}/api-token/verify/`
const REGISTER_URL = `${API_BASE}/rest-auth/registration/`

export default {
  API_BASE,
  LOGIN_URL,
  VERIFY_URL,
  REGISTER_URL
}
