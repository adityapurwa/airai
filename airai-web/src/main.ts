import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";

import { VueQueryPlugin } from "vue-query";
import { router } from "./routes";

const app = createApp(App);
app.use(VueQueryPlugin);
app.use(router);
app.mount("#app");
