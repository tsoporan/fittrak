<template>
  <v-navigation-drawer app persistent clipped v-model="drawer">
  <ul>
    <li>
      <router-link to="/home">
        Track 
      </router-link>
    </li>

    <li>
      <router-link to="/progress">
        Progress
      </router-link>
    </li>

    <li>
      <router-link to="/history">
        History
      </router-link>
    </li>

    <li>
      <router-link to="/settings">
        Settings
      </router-link>
    </li>

    <li>
      <a href="" @click.prevent="logout">
        <span class="icon is-small"><i class="fa fa-sign-out" aria-hidden="true"></i></span>
        Logout
      </a>
    </li>
  </ul>

  <div class="sidebar-footer">
    <p>Made with <span style="color:red;">&#10084;</span> by <a href="https://github.com/tsoporan/fittrack">tsoporan</a></p>
  </div>

</v-navigation-drawer>
</template>

<script>
import auth from '../auth'

export default {
  props: ['drawer'],
  methods: {
    logout () {
      return auth.logout()
    }
  }
}
</script>
