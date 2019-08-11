import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

export default new Vuetify({
  icons: {
    iconfont: "mdi"
  },
  theme: {
    themes: {
      light: {
        primary: "#06d6a0",
        secondary: "#26547c",
        accent: "#4ce0d2",
        error: "#d62246",
        info: "#26547c",
        success: "#06d6a0",
        warning: "#ffd166",
        mainBg: "#fafafa",
        primaryDark: "#00ae80",
        darkGrey: "#424242"
      }
    }
  }
});
