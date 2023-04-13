import axios from "axios";
import { api } from "./api";
import { useQuery } from "vue-query/esm";
import { UseQueryOptions } from "vue-query";
import { Ref } from "vue";

export function chat(query: string) {
  return api.get("api/v1/chat", { params: { query: query } });
}

export function useChatQuery(query: Ref<string>) {
  return useQuery(["chat", query], () => chat(query.value), { enabled: false });
}

export const ERROR_NOT_ASKING_ABOUT_AIR_QUALITY =
  "NOT_ASKING_ABOUT_AIR_QUALITY";

export const ERROR_NO_QUERY = "NO_QUERY";
export const ERROR_QUERY_TOO_LONG = "QUERY_TOO_LONG";
