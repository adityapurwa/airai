import axios, { AxiosError, AxiosPromise, AxiosResponse } from "axios";
import { reactive, UnwrapNestedRefs, UnwrapRef } from "vue";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export function useApi<
  T,
  F extends (...args: Parameters<F>) => AxiosPromise<T>
>(
  fn: F
): [
  UnwrapNestedRefs<{
    data: T | null;
    error: Error | AxiosError | unknown;
    loading: boolean;
  }>,
  F
] {
  const state = reactive<{
    data: T | null;
    error: Error | AxiosError | unknown;
    loading: boolean;
  }>({
    data: null,
    error: null,
    loading: false,
  });
  const invoke: (...args: Parameters<F>) => AxiosPromise<T> = (...args) => {
    state.loading = true;
    return fn(...args)
      .then((response: AxiosResponse<T>) => {
        state.data = response.data as UnwrapRef<T>;
        state.error = null;
        state.loading = false;
        return response;
      })
      .catch((error: AxiosError) => {
        state.error = error;
        state.loading = false;
        throw error;
      });
  };
  return [state, invoke as F];
}
