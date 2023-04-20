<script setup lang="ts">
import { getDynamicBackground } from "./lib/ui/background";
import HeaderNavigation from "./components/navigations/header-navigation/HeaderNavigation.vue";

const bgForTime = getDynamicBackground();
</script>

<template>
  <div
    class="flex h-[100vh] w-full flex-col items-center justify-center p-4"
    :style="{
      backgroundImage: `url(${bgForTime})`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
    }"
  >
    <HeaderNavigation class="mb-4"></HeaderNavigation>
    <router-view></router-view>
    <footer
      class="mt-4 rounded-lg bg-white bg-opacity-90 p-2 text-xs backdrop-blur-xl"
    >
      <a href="https://github.com/adityapurwa/airai">Open Source AGPL v3 - Aditya</a>
    </footer>
  </div>
</template>
