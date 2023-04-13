import { computed } from "vue";

export function getDynamicBackground() {
  const now = new Date();

  if (now.getHours() <= 7) {
    return "/bg/dawn.jpg";
  }
  if (now.getHours() <= 15) {
    return "/bg/day.jpg";
  }
  if (now.getHours() <= 19) {
    return "/bg/dusk.jpg";
  }
  return "/bg/night.jpg";
}
