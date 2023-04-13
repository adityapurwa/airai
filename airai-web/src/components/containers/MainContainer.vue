<template>
  <div
    v-bind="$attrs"
    class="flex h-0 w-full max-w-3xl flex-shrink flex-grow flex-col rounded-lg bg-white bg-opacity-50 shadow-2xl backdrop-blur-3xl"
  >
    <slot></slot>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped></style>
