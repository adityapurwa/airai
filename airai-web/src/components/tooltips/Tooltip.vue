<template>
  <div
    ref="slot"
    @mouseenter="tooltipVisible = true"
    @mouseleave="tooltipVisible = false"
  >
    <slot></slot>
  </div>
  <teleport to="body">
    <div ref="tooltip">
      <slot name="tooltip"></slot>
    </div>
  </teleport>
</template>

<script lang="ts" setup>
import { ref, watch } from "vue";
import { createPopper, Instance } from "@popperjs/core";

const slot = ref<HTMLElement>();
const tooltip = ref<HTMLElement>();
const tooltipVisible = ref(false);
const popperRef = ref<Instance>();

watch(tooltipVisible, (visible) => {
  if (visible) {
    popperRef.value = createPopper(slot.value!, tooltip.value!, {
      placement: "top",
      modifiers: [
        {
          name: "offset",
          options: {
            offset: [0, 8],
          },
        },
      ],
    });
  } else {
    popperRef.value?.destroy();
  }
});
</script>
