<template>
  <v-row v-if="!loading" justify="center">
    <v-col v-for="(item, index) in dolares" :key="index" cols="4" lg="3">
      <ResumenCard
        :id="item.id"
        :name="item.nombre"
        :description="item.detalle"
        :imgroute="item.urlimagen"
        :type="item.idtipo"
        :rating="item.rating"
      />
    </v-col>

    <v-col cols="4" lg="3" class="pa-4 my-auto">
      <v-btn color="primary" nuxt to="/agregar-medio"
        ><span><v-icon>mdi-plus</v-icon> Agregar </span>
      </v-btn>
    </v-col>
  </v-row>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'IndexPage',
  data() {
    return {
      dolares: {},
      uf: {},
      loading: true,
    }
  },
  async mounted() {
    this.loading = true
    this.dolares = await this.getCurrencyUSD()
    this.uf = await this.getCurrencyUF()
    this.dolares.forEach((element) => {
      console.log(element)
    })
    this.uf.forEach((index) => {
      console.log(index)
    })
    this.loading = false
  },
  methods: {
    ...mapActions({
      getCurrencyUSD: 'getCurrencyUSD',
      getCurrencyUF: 'getCurrencyUF',
    }),
  },
}
</script>
