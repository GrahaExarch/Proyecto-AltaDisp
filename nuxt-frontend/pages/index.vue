<template>
  <v-row justify="center">
    <v-col cols="4" lg="3">
      <ResumenCard type="USD" />
    </v-col>
    <v-col cols="4" lg="3">
      <ResumenCard type="UF" />
    </v-col>
    <v-col cols="4" lg="3"> temperatura </v-col>
    <v-col cols="4" lg="3">
      <v-card align="center">
        <v-card-title class="headline"> Crucigrama Online: </v-card-title>
        <v-btn class="mx-auto" color="primary"
          ><a href="https://www.emol.com/servicios/juegos/crucigrama.aspx">
            Ir
          </a></v-btn
        >
      </v-card></v-col
    >
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>

<style scoped>
.v-application a {
  color: white;
}
</style>
