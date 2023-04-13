<template>
  <MainContainer>
    <div
      class="flex flex-shrink flex-grow flex-col items-center justify-center gap-4"
      v-if="data.length === 0"
    >
      <div class="flex items-center gap-4">
        <img src="/airai.svg" alt="AirAI" class="h-24 w-24" />
        <div>
          <h1 class="text-8xl font-extralight">AirAI</h1>
          <h2 class="font-normal opacity-75">
            GPT Powered Air Quality Dashboard
          </h2>
        </div>
      </div>
      <AppButton
        v-if="showGeolocateButton"
        :disabled="geocodeState.loading || chatState.loading"
        :is-loading="geocodeState.loading"
        @click="getUserLocationAsPrompt"
        type="button"
        class="mt-12 text-xs"
      >
        Air Quality In My Location
      </AppButton>
    </div>
    <div v-else class="my-4 flex-shrink flex-grow overflow-y-auto p-4">
      <div
        class="mb-4 grid gap-4"
        v-for="collection in data"
        :style="{
          gridTemplateColumns: `repeat(${collection.length}, 1fr)`,
        }"
      >
        <AirQualityCard v-for="item in collection" :data="item" />
      </div>
    </div>
    <div
      class="mx-8 rounded-t-lg bg-red-100 p-2 text-sm text-red-700"
      @click="error = undefined"
      v-if="error"
    >
      {{ error }}
    </div>
    <div class="mx-4 rounded-t-2xl bg-white p-4 backdrop-blur-3xl">
      <form @submit.prevent="ask">
        <div class="flex items-center gap-2">
          <div class="flex-shrink flex-grow">
            <AppInputField
              maxlength="150"
              v-model="prompt"
              placeholder="E.g How is the air quality in Paris?"
              required
              autofocus
              :disabled="chatState.loading"
              ref="promptRef"
            />
          </div>
          <AppButton
            :disabled="geocodeState.loading || chatState.loading"
            :is-loading="chatState.loading"
            type="submit"
          >
            Ask
          </AppButton>
        </div>
      </form>
    </div>
  </MainContainer>
</template>

<script lang="ts" setup>
import AppButton from "../../components/buttons/PrimaryButton.vue";
import AppInputField from "../../components/forms/AppInputField.vue";
import AirQualityCard from "./components/cards/AirQualityCard.vue";
import { useGeolocation } from "@vueuse/core";
import { useApi } from "../../lib/api/api";
import { geocodeFromCoordinate } from "../../lib/api/geocode";
import {
  chat,
  ERROR_NO_QUERY,
  ERROR_NOT_ASKING_ABOUT_AIR_QUALITY,
  ERROR_QUERY_TOO_LONG,
} from "../../lib/api/chat";
import { computed, ref } from "vue";
import MainContainer from "../../components/containers/MainContainer.vue";
import { meteoTimeToDate } from "../../lib/aqi/aqi";
import { AxiosError } from "axios";
const uGeo = useGeolocation();
const [geocodeState, invokeGeocodeFromCoordinate] = useApi(
  geocodeFromCoordinate
);
const [chatState, invokeChat] = useApi(chat);

const prompt = ref("");
const promptRef = ref<HTMLInputElement>();
const data = ref<any>([]);

const error = ref<string>();

async function ask() {
  error.value = undefined;
  if (prompt.value) {
    try {
      const res = await invokeChat(prompt.value);
      if (res.data) {
        prompt.value = "";
        promptRef.value?.focus();
        const airQualities = res.data.air_qualities;
        if (!Array.isArray(airQualities)) {
          error.value =
            "AirAI can only response to inquiries about air quality, e.g 'How is the air quality in Paris?'";
        }
        // we want to mutate straight away to avoid post-processing on other components
        for (const entry of airQualities) {
          entry.hourly.time = entry.hourly.time.map(meteoTimeToDate);
        }
        data.value.push(airQualities);
      }
    } catch (e) {
      console.log(e);
      if (e instanceof AxiosError) {
        console.log(e.status);
        if (e.response?.status === 400) {
          if (e.response?.data.detail === ERROR_NOT_ASKING_ABOUT_AIR_QUALITY) {
            error.value =
              "AirAI can only response to inquiries about air quality";
          }
          if (e.response?.data.detail === ERROR_NO_QUERY) {
            error.value = "Your message is empty";
          }
          if (e.response?.data.detail === ERROR_QUERY_TOO_LONG) {
            error.value =
              "Your message is too long, keep it less than 150 characters";
          }
        }
        if (e.response?.status === 429) {
          if (e.response?.data.detail === ERROR_NOT_ASKING_ABOUT_AIR_QUALITY) {
            error.value =
              "You have reached the maximum number of 5 request per minute, please wait a bit before asking again";
          }
        }
      }
    }
  }
}

async function getUserLocationAsPrompt() {
  uGeo.resume();
  if (uGeo.coords.value.latitude && uGeo.coords.value.longitude) {
    const res = await invokeGeocodeFromCoordinate({
      latitude: uGeo.coords.value.latitude,
      longitude: uGeo.coords.value.longitude,
    });
    if (res.data.locality) {
      prompt.value = `How is the air quality in ${res.data.locality}?`;
      ask();
    }
  }
  uGeo.pause();
}

const showGeolocateButton = computed(
  () => uGeo.isSupported && uGeo.error.value?.code !== 1
);
</script>

<style scoped></style>
