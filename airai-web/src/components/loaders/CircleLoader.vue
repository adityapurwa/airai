<template>
  <div class="circle-loader" v-bind="$attrs"></div>
</template>

<script setup lang="ts"></script>

<style scoped>
.circle-loader {
  border: currentColor 2px solid;
  border-radius: 10000px;
  border-top-color: transparent;
  animation: spin 1s linear infinite;
  width: 1.5em;
  height: 1.5em;
}
@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>
