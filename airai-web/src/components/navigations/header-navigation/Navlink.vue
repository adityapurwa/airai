<template>
  <router-link
    :to="to"
    class="block rounded bg-gray-100 px-2 py-1 font-sans uppercase text-black opacity-50"
    active-class="shadow-lg !opacity-100 bg-white"
  >
    <slot></slot>
  </router-link>
</template>

<script setup lang="ts">
const props = defineProps<{
  to: string;
}>();
</script>

<style scoped></style>
