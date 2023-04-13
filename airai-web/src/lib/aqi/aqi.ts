export const THRESHOLD_COLOR = [
  "#84c1e7",
  "#88e0a1",
  "#dad677",
  "#aa7ee0",
  "#ce93a8",
  "#f85555",
];
export const THRESHOLD_LABELS = [
  "Good",
  "Moderate",
  "Unhealthy for Sensitive Groups",
  "Unhealthy",
  "Very Unhealthy",
  "Hazardous",
];
export const PM_2_5_THRESHOLD = [10, 20, 25, 50, 75, 800];
export const PM_10_THRESHOLD = [20, 40, 50, 100, 150, 1200];
export const NO2_THRESHOLD = [40, 90, 120, 230, 340, 1000];
export const O3_THRESHOLD = [50, 100, 130, 240, 380, 800];
export const SO2_THRESHOLD = [100, 200, 350, 500, 750, 1250];
export const AQI_THRESHOLD = [20, 40, 60, 80, 100, 1000];

export function getThresholdIndex(value: number, threshold: number[]) {
  for (let i = 0; i < threshold.length; i++) {
    if (value <= threshold[i]) {
      return i;
    }
  }
  return threshold.length - 1;
}

export function meteoTimeToDate(time: string) {
    return new Date(time + ":00.000Z");
}