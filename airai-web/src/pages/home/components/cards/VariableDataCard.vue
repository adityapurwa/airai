<template>
  <div
    @click="uiState.showDetail = true"
    class="flex flex-shrink flex-grow cursor-pointer flex-col justify-center rounded p-4 text-center transition-all hover:bg-gray-100"
    :style="{
      borderBottom: `8px solid ${colorCode}`,
    }"
  >
    <dd class="text-3xl font-light text-gray-800">
      <slot name="value"></slot>
    </dd>
    <dt class="text-sm text-gray-500">
      <slot name="label"></slot>
    </dt>
  </div>
  <teleport to="body" v-if="uiState.showDetail">
    <div
      @click.self="uiState.showDetail = false"
      class="fixed left-0 top-0 flex h-full w-full items-center justify-center bg-black bg-opacity-50"
    >
      <div
        class="max-h-[80vh] min-w-[75vw] max-w-[80vw] overflow-y-auto rounded-md bg-white shadow-2xl"
      >
        <div class="m-10 flex gap-8">
          <div>
            <h3 class="text-4xl font-light text-black text-opacity-50">
              <slot name="label"></slot>
            </h3>
            <h4 class="text-8xl font-extralight">
              <slot name="value"></slot>
            </h4>
          </div>
          <div class="flex-shrink flex-grow text-gray-700">
            <div
              class="my-2 inline-block rounded p-2 text-sm font-semibold"
              :style="{
                backgroundColor: THRESHOLD_COLOR[thresholdIndex],
              }"
            >
              {{ THRESHOLD_LABELS[thresholdIndex] }}
            </div>
            <slot name="description"></slot>
          </div>
        </div>
        <div class="m-10">
          <h3 class="text-center text-xl">History &amp; Prediction</h3>
          <NeutraltextBlock class="my-5">
            You can hover over the data points to see the exact value.
          </NeutraltextBlock>
          <div class="relative my-4 grid grid-cols-2 gap-8">
            <div
              v-for="(group, index) in groupedCombinedDataByDay"
              class="flex-shrink flex-grow"
            >
              <div class="flex flex-col items-center gap-2 rounded">
                <div class="w-full text-center text-xs font-semibold">
                  {{ group.time.toLocaleDateString() }}
                </div>
                <div
                  class="flex w-full items-center gap-0.5 rounded-sm bg-white"
                >
                  <div
                    v-for="item in group.entries"
                    class="flex-shrink flex-grow text-center text-xs"
                  >
                    <Tooltip>
                      <div
                        class="h-4 select-none transition-all hover:translate-y-[-2px]"
                        :style="{
                          backgroundColor:
                            THRESHOLD_COLOR[
                              getThresholdIndex(item.value, props.threshold)
                            ],
                        }"
                      >
                        {{ item.active ? "Now" : "" }}
                      </div>
                      <template #tooltip>
                        <div class="flex items-center text-xs text-gray-900">
                          <div class="rounded-l bg-gray-200 p-1">
                            {{
                              item.time.getHours().toString().padStart(2, "0")
                            }}:{{
                              item.time.getMinutes().toString().padStart(2, "0")
                            }}
                          </div>
                          <div class="rounded-r bg-gray-900 p-1 text-gray-100">
                            {{ item.value }}
                          </div>
                        </div>
                      </template>
                    </Tooltip>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </teleport>
</template>
<script setup lang="ts">
import { computed, reactive } from "vue";
import {
  getThresholdIndex,
  THRESHOLD_COLOR,
  THRESHOLD_LABELS,
} from "../../../../lib/aqi/aqi";
import Tooltip from "../../../../components/tooltips/Tooltip.vue";
import NeutraltextBlock from "../../../../components/textblock/NeutraltextBlock.vue";

const props = defineProps<{
  threshold: number[];
  value: number;
  data: number[];
  time: Date[];
  activeIndex: number;
}>();

const uiState = reactive({
  showDetail: false,
});

const combinedDataTime = computed(() => {
  return props.data
    .map((item, index) => {
      return {
        value: item,
        time: props.time[index],
      };
    })
    .filter((item) => item.value !== null);
});

const groupedCombinedDataByDay = computed(() => {
  const timeGroups: any = {};
  combinedDataTime.value.forEach((item, index) => {
    const date = new Date(item.time);
    const day = `${date.getFullYear()}-${date.getMonth()}-${date.getDate()}`;
    if (!timeGroups[day]) {
      timeGroups[day] = {
        entries: [],
        time: new Date(day),
      };
    }
    const isActive = props.activeIndex === index;
    if (isActive) {
      timeGroups[day].entries.push({ ...item, active: true });
    } else {
      timeGroups[day].entries.push(item);
    }
  });
  return timeGroups;
});

const thresholdIndex = computed(() => {
  return getThresholdIndex(props.value, props.threshold);
});

const colorCode = computed(() => {
  return THRESHOLD_COLOR[getThresholdIndex(props.value, props.threshold)];
});
</script>
