<template>
  <input
    ref="inputRef"
    v-bind="$attrs"
    class="w-full rounded-md bg-gray-200 px-4 py-2 text-gray-800 placeholder-gray-500 outline-none disabled:opacity-50"
    :value="modelValue"
    @input="$emit('update:modelValue', inputRef?.value)"
  />
</template>
<script setup lang="ts">
import { ref } from "vue";

const props = defineProps({
  modelValue: {
    type: String,
    default: "",
  },
});

const inputRef = ref<HTMLInputElement>();
const focus = () => {
  inputRef.value?.focus();
};

defineExpose({
  focus,
});
</script>
