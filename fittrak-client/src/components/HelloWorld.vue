<template>
  <div>Hello {{ msg }}</div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String
  }
};
</script>

<style scoped>
</style>
