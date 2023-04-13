<template>
  <button
    v-bind="$attrs"
    class="rounded-md bg-gray-800 px-4 py-2 text-base text-gray-200 outline-monte transition-all hover:bg-gray-700 disabled:opacity-50"
  >
    <CircleLoader v-if="isLoading"/>
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
