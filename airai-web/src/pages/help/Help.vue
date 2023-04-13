<template>
  <MainContainer class="overflow-y-auto bg-opacity-90 p-8">
    <article>
      <h1 class="text-4xl font-light">Help on Using AirAI</h1>
      <h2 class="my-4 font-semibold">Getting Air Quality</h2>
      <p class="leading-12 my-2">
        AirAI is operated using a chat interface. To get an air quality data,
        simply type into the chat input at the bottom using natural language and
        mentioning the city name. For example, you can type:
      </p>
      <SampletextBlock class="my-4">
        How is the air quality in Paris?
      </SampletextBlock>
      <p class="leading-12 my-2">
        You can also click on "Air Quality In My Location" to get the air
        quality in your current location. Note that this feature requires your
        browser to have access to your location.
      </p>
      <p class="leading-12 my-2">You can also query multiple cities:</p>
      <SampletextBlock class="my-4">
        How is the air quality in the capital of Japan and Korea?
      </SampletextBlock>

      <h2 class="my-4 font-semibold">Understanding Color Code</h2>
      <p class="leading-12 my-2">
        The color code is based on the European air quality index (AQI) which is
        a measurement of the air quality. The AQI is calculated based on the
        concentration of pollutants in the air. The AQI is divided into 6
        categories:
      </p>
      <ul class="my-8 flex flex-col gap-4">
        <ColorCode :color="THRESHOLD_COLOR[0]">Good</ColorCode>
        <ColorCode :color="THRESHOLD_COLOR[1]">Moderate</ColorCode>
        <ColorCode :color="THRESHOLD_COLOR[2]"
          >Unhealthy for Sensitive Groups</ColorCode
        >
        <ColorCode :color="THRESHOLD_COLOR[3]">Unhealthy</ColorCode>
        <ColorCode :color="THRESHOLD_COLOR[4]">Very Unhealthy</ColorCode>
        <ColorCode :color="THRESHOLD_COLOR[5]">Hazardous</ColorCode>
      </ul>
      <h2 class="my-4 font-semibold">Detailed Information</h2>
      <p class="leading-12 my-2">
        You can click on each individual metrics to get more insights about it.
      </p>
      <h2 class="my-4 font-semibold">Fair Use</h2>
      <p class="leading-12 my-2">
        AirAI is a free service. To keep the service running, we need to limit
        the number of requests per user to 5 messages per minute.
      </p>
    </article>
  </MainContainer>
</template>

<script setup lang="ts">
import MainContainer from "../../components/containers/MainContainer.vue";
import { THRESHOLD_COLOR } from "../../lib/aqi/aqi";
import ColorCode from "./components/ColorCode.vue";
import SampletextBlock from "../../components/textblock/SampletextBlock.vue";
</script>

<style scoped></style>
