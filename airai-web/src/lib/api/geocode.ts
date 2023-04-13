import { api } from "./api";
import { useQuery } from "vue-query/esm";
import { Ref } from "vue";

export function geocodeFromCoordinate(coordinate: {
  latitude: number;
  longitude: number;
}) {
  return api.get<{
    locality: string;
  }>(`https://api.bigdatacloud.net/data/reverse-geocode-client`, {
    params: {
      query: {
        latitude: coordinate.latitude,
        longitude: coordinate.longitude,
        localityLanguage: "en",
      },
    },
  });
}

export function useGeocodeFromCoordinateQuery(
  coordinate: Ref<{
    latitude: number;
    longitude: number;
  }>
) {
  return useQuery(
    ["geocode", coordinate],
    () => geocodeFromCoordinate(coordinate.value),
    { enabled: false }
  );
}
