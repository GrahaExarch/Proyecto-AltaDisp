<template>
  <v-row justify="center">
    <v-col cols="4" lg="3">
      <ResumenCard type="USD" />
    </v-col>
    <v-col cols="4" lg="3">
      <ResumenCard type="UF" />
    </v-col>
    <v-col cols="4" lg="3"> crucigrama </v-col>
    <v-col cols="4" lg="3"> temperatura </v-col>
  </v-row>
</template>

<script>
export default {
  name: 'IndexPage',
}
</script>
