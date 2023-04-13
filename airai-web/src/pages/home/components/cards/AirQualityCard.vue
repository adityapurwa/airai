<template>
  <div class="bg-opacity-750 rounded-md bg-white backdrop-blur-xl">
    <header
      class="flex items-center border-b-2 border-gray-200 p-4 text-2xl font-light gap-2"
    >
      <h3 class="flex-shrink flex-grow">
        {{ data.city }}
      </h3>
      <div
        class="rounded p-2 text-xl"
        :style="{
          backgroundColor:
            THRESHOLD_COLOR[
              getThresholdIndex(
                data.hourly.european_aqi[currentHourlyIndex],
                AQI_THRESHOLD
              )
            ],
        }"
      >
        {{ data.hourly.european_aqi[currentHourlyIndex] }}
      </div>
    </header>
    <div class="m-4">
      <img
        v-if="shouldShowMap"
        :src="`https://maps.googleapis.com/maps/api/staticmap?key=${MAP_API_KEY}&zoom=9&size=1200x600&center=${data.latitude},${data.longitude}`"
        :alt="data.city"
        @error="shouldShowMap = false"
        class="h-48 w-full rounded object-cover"
      />
    </div>
    <div class="m-4 flex flex-wrap justify-center gap-4">
      <DataLabelCard
        :active-index="currentHourlyIndex"
        :data="data.hourly.european_aqi_pm2_5"
        :time="data.hourly.time"
        :threshold="PM_2_5_THRESHOLD"
        :value="data.hourly.european_aqi_pm2_5[currentHourlyIndex]"
      >
        <template #value>
          {{ data.hourly.european_aqi_pm2_5[currentHourlyIndex] }}
        </template>
        <template #label>
          PM<span class="align-super text-base">2.5</span>
        </template>
        <template #description>
          <p class="leading-relaxed">
            PM2.5 stands for fine particulate matter with a diameter of less
            than 2.5 micrometers. These particles can come from sources such as
            vehicle exhaust, industrial emissions, and wildfires. PM2.5 can
            penetrate deep into the lungs and bloodstream, causing respiratory
            and cardiovascular problems.
          </p>
          <InfotextBlock class="my-4">
            To reduce exposure, individuals can avoid exercising or spending
            extended periods of time outdoors when pollution levels are high,
            use air purifiers in indoor spaces, and wear masks designed to
            filter out PM2.5 particles.
          </InfotextBlock>
        </template>
      </DataLabelCard>
      <DataLabelCard
        :active-index="currentHourlyIndex"
        :data="data.hourly.european_aqi_pm10"
        :time="data.hourly.time"
        :threshold="PM_10_THRESHOLD"
        :value="data.hourly.european_aqi_pm10[currentHourlyIndex]"
      >
        <template #value>
          {{ data.hourly.european_aqi_pm10[currentHourlyIndex] }}
        </template>
        <template #label> PM<span class="align-super">10</span> </template>
        <template #description>
          <p class="leading-relaxed">
            PM10 stands for particulate matter with a diameter of less than 10
            micrometers. Sources of PM10 include dust, vehicle exhaust, and
            industrial emissions. PM10 can cause respiratory and cardiovascular
            problems.
          </p>
          <InfotextBlock class="my-4">
            To reduce exposure, individuals can avoid exercising or spending
            extended periods of time outdoors when pollution levels are high,
            use air purifiers in indoor spaces, and wear masks designed to
            filter out PM10 particles.
          </InfotextBlock>
        </template>
      </DataLabelCard>
      <DataLabelCard
        :active-index="currentHourlyIndex"
        :data="data.hourly.european_aqi_no2"
        :time="data.hourly.time"
        :threshold="NO2_THRESHOLD"
        :value="data.hourly.european_aqi_no2[currentHourlyIndex]"
      >
        <template #value>
          {{ data.hourly.european_aqi_no2[currentHourlyIndex] }}
        </template>
        <template #label> NO<span class="align-super">2</span> </template>
        <template #description>
          <p class="leading-relaxed">
            NO2 is a gas that is produced by the burning of fossil fuels, such
            as those used in transportation and industry. Exposure to high
            levels of NO2 can cause respiratory problems.
          </p>
          <InfotextBlock class="my-4">
            Reduce exposure by avoiding busy roads and intersections, using
            public transportation, and supporting policies that promote the use
            of clean energy sources.
          </InfotextBlock>
        </template>
      </DataLabelCard>
      <DataLabelCard
        :active-index="currentHourlyIndex"
        :data="data.hourly.european_aqi_o3"
        :time="data.hourly.time"
        :threshold="O3_THRESHOLD"
        :value="data.hourly.european_aqi_o3[currentHourlyIndex]"
      >
        <template #value>
          {{ data.hourly.european_aqi_o3[currentHourlyIndex] }}
        </template>
        <template #label> O<span class="align-super">3</span> </template>
        <template #description>
          <p class="leading-relaxed">
            Ozone is a gas that is formed when sunlight reacts with pollutants
            in the air, such as those emitted by vehicles and industrial
            sources. Ozone can cause respiratory problems and aggravate existing
            lung conditions.
          </p>
          <InfotextBlock class="my-4">
            Individuals can reduce exposure by avoiding outdoor exercise during
            periods of high pollution, using air purifiers in indoor spaces, and
            supporting policies that promote the use of clean energy sources.
          </InfotextBlock>
        </template>
      </DataLabelCard>
      <DataLabelCard
        :active-index="currentHourlyIndex"
        :data="data.hourly.european_aqi_so2"
        :time="data.hourly.time"
        :threshold="SO2_THRESHOLD"
        :value="data.hourly.european_aqi_so2[currentHourlyIndex]"
      >
        <template #value>
          {{ data.hourly.european_aqi_so2[currentHourlyIndex] }}
        </template>
        <template #label> SO<span class="align-super">2</span> </template>
        <template #description>
          <p class="leading-relaxed">
            SO2 is a gas that is produced by the burning of fossil fuels, such
            as coal and oil. Exposure to high levels of SO2 can cause
            respiratory problems.
          </p>
          <InfotextBlock class="my-4">
            Reduce exposure by supporting policies that promote the use of clean
            energy sources and reducing personal use of fossil fuels.
          </InfotextBlock>
        </template>
      </DataLabelCard>
    </div>
    <div class="m-4">
      <div
        v-if="
          getThresholdIndex(
            data.hourly.european_aqi[currentHourlyIndex],
            AQI_THRESHOLD
          ) > 2
        "
        class="rounded bg-red-200 p-3 text-sm"
      >
        <p class="font-bold text-red-950">Air quality is unhealthy</p>
        <p>
          People with heart or lung disease, older adults, and children should
          avoid prolonged outdoor exertion. Wear a mask to protect your health.
        </p>
      </div>
      <div
        v-else-if="
          getThresholdIndex(
            data.hourly.european_aqi[currentHourlyIndex],
            AQI_THRESHOLD
          ) > 1
        "
        class="rounded bg-orange-200 p-3 text-sm"
      >
        <p class="font-bold text-orange-950">Air quality is not optimal</p>
        <p>Wear mask</p>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { computed, ref } from "vue";
import DataLabelCard from "./VariableDataCard.vue";
import {
  AQI_THRESHOLD,
  getThresholdIndex,
  NO2_THRESHOLD,
  O3_THRESHOLD,
  PM_10_THRESHOLD,
  PM_2_5_THRESHOLD,
  SO2_THRESHOLD,
  THRESHOLD_COLOR,
} from "../../../../lib/aqi/aqi";
import InfotextBlock from "../../../../components/textblock/InfotextBlock.vue";

const MAP_API_KEY = import.meta.env.VITE_STATIC_MAP_KEY;
const props = defineProps<{
  data: {
    city: string;
    latitude: number;
    longitude: number;
    hourly: {
      time: Date[];
      european_aqi: number[];
      european_aqi_pm2_5: number[];
      european_aqi_pm10: number[];
      european_aqi_no2: number[];
      european_aqi_o3: number[];
      european_aqi_so2: number[];
    };
  };
}>();

const shouldShowMap = ref(Boolean(MAP_API_KEY));

const timeframe = new Date();
timeframe.setMinutes(0, 0, 0);
const timeframeIso = timeframe.toISOString();

const currentHourlyIndex = computed(() => {
  return props.data.hourly.time.findIndex(
    (time) => time.toISOString() === timeframeIso
  );
});
</script>
