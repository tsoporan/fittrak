<template>
  <div class="landing">
    {{ hello }} with GraphQL
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'Landing',
  apollo: {
    hello: gql`{hello}`
  },
  data () {
    return {
      hello: ''
    }
  }
}
</script>
