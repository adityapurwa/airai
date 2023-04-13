<template>
  <header
    class="mb-4 flex w-full max-w-3xl items-center justify-start rounded-lg bg-white bg-opacity-25 p-2 shadow-2xl backdrop-blur-3xl"
  >
    <nav>
      <ul class="flex items-center gap-2 text-sm">
        <li>
          <Navlink to="/"> Home </Navlink>
        </li>
        <li>
          <Navlink to="/help"> Help </Navlink>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script setup lang="ts">
import Navlink from "./Navlink.vue";
</script>

<style scoped></style>
