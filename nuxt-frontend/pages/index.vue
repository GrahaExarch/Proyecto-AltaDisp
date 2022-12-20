<template>
  <v-row justify="center">
    <v-col cols="6">
      <v-card v-if="!loading" class="fill-height" align="center" elevation="10">
        <p class="text-center text-h4">Divisas</p>
        <ResumenCard class="mb-6" type="USD" />
        <ResumenCard type="UF" />
      </v-card>
    </v-col>
    <v-col cols="6">
      <v-card v-if="!loading" align="center" elevation="10">
        <v-card-text class="text-center">
          <p class="text-h4">Santiago</p>
          <div class="align-center d-flex justify-center">
            <p class="text-h1 my-0">
              {{ weather.main.temp | number }}
            </p>
            <v-icon size="36">mdi-temperature-celsius</v-icon>
          </div>
          <div class="align-center d-flex justify-center">
            <p class="text-h5 my-0">
              {{ weather.weather[0].description | capitalize }}
            </p>
            <img :src="url" />
          </div>

          <div class="align-center d-flex justify-center">
            <span class="text-h4 my-0 mr-3">
              Max: {{ weather.main.temp_max | number }}°
            </span>
            <span class="text-h4 my-0">
              Min:
              {{ weather.main.temp_min | number }}°
            </span>
          </div>
          <div class="align-center d-flex justify-center">
            <v-icon>mdi-thermometer</v-icon>
            <v-icon class="ml-n2">mdi-account</v-icon>
            <span class="text-h6 my-0">
              {{ weather.main.feels_like | number }}°</span
            >
            <span class="text-h5 font-weight-bold mx-2">|</span>
            <v-icon>mdi-weather-windy</v-icon>
            <span class="text-h6 my-0"
              >{{ weather.wind.speed | number }} kph</span
            >
          </div>
        </v-card-text>
      </v-card>
    </v-col>

    <v-col cols="6">
      <v-card align="center" elevation="10">
        <v-card-text class="d-flex flex-row align-center justify-center">
          <span class="text-h4">Crucigrama Online:</span>

          <v-btn
            class="mx-auto"
            color="primary"
            href="https://www.emol.com/servicios/juegos/crucigrama.aspx"
            >Ir</v-btn
          >
        </v-card-text>
      </v-card></v-col
    >
  </v-row>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'IndexPage',
  data() {
    return {
      weather: [],
      url: 'http://openweathermap.org/img/wn/{icon}.png',
      dialog: false,
      loading: true,
    }
  },
  async mounted() {
    this.loading = true
    this.weather = await this.getWeather()
    this.url = this.url.replace('{icon}', this.weather.weather[0].icon)
    this.loading = false
  },
  methods: {
    ...mapActions({
      getWeather: 'getWeather',
    }),
  },
}
</script>

<style scoped></style>
