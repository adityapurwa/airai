<template>
  <button
    v-bind="$attrs"
    class="rounded-md bg-gray-100 px-4 py-2 text-gray-700 outline-monte transition-all hover:bg-gray-300 disabled:opacity-50"
  >
    <CircleLoader v-if="isLoading" />
    <slot v-else />
  </button>
</template>
<script setup lang="ts">
import CircleLoader from "../loaders/CircleLoader.vue";

const props = defineProps({
  isLoading: {
    type: Boolean,
    default: false,
  },
});
</script>
