<template>
  <li class="flex items-center gap-2">
    <div
      class="h-6 w-6 rounded"
      :style="{
        background: color,
      }"
    ></div>
    <slot></slot>
  </li>
</template>

<script lang="ts" setup>
import { THRESHOLD_COLOR } from "../../../lib/aqi/aqi";

const props = defineProps<{ color: string }>();
</script>

<style scoped></style>
