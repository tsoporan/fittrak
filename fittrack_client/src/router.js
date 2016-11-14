import Vue from 'vue'
import VueRouter from 'vue-router'

import Index from './components/Index'
import Home from './components/Home'
import Login from './components/Login'
import Register from './components/Register'
import NewWorkout from './components/NewWorkout'
import Progress from './components/Progress'
import Settings from './components/Settings'
import History from './components/History'

import auth from './auth'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Index },
  { path: '/home', component: Home, meta: { requiresAuth: true } },
  { path: '/newworkout', component: NewWorkout, meta: { requiresAuth: true } },
  { path: '/progress', component: Progress, meta: { requiresAuth: true } },
  { path: '/settings', component: Settings, meta: { requiresAuth: true } },
  { path: '/history', component: History, meta: { requiresAuth: true } },
  { path: '/login', component: Login },
  { path: '/register', component: Register },
  { path: '/*', component: Index }
]

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

// Need to ensure that we protect auth-dependent endpoints
router.beforeEach((to, from, next) => {
  // On refresh of index route if you are logged in take you home
  if (to.path === '/' && auth.getToken()) {
    return next({ path: '/home' })
  }

  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    auth.checkAuth().then((res) => {
      console.log('**** router check auth success')
      next()
    }, (res) => {
      console.log('**** router check auth failure')
      // Failed auth
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    })
  } else {
    next() // make sure to always call next()!
  }
})

export default router
