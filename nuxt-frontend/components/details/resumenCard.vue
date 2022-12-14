<template>
  <v-card v-if="!loading" align="center">
    <v-card-title class="headline"> El valor de {{ type }} es: </v-card-title>
    <v-card-text>
      <p class="overflow-auto text-h4 font-weight-bold">
        {{ todayCurrency.value }}
      </p>
      <hr class="my-3" />
    </v-card-text>
    <v-card-actions>
      <v-btn class="mx-auto" color="primary" @click="dialog = true">
        Historico
      </v-btn>
    </v-card-actions>
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="text-h5">
          Valor Historico de {{ type }}
        </v-card-title>

        <v-card-text>
          <v-simple-table fixed-header height="300px">
            <template #default>
              <thead>
                <tr>
                  <th class="text-left">Fecha</th>
                  <th class="text-left">Valor</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="currency.length === 0">
                  <td>No hay mas registros</td>
                </tr>
                <template v-else>
                  <tr v-for="(item, index) in currency" :key="index">
                    <td>{{ item.date }}</td>
                    <td>{{ item.value }}</td>
                  </tr>
                </template>
              </tbody>
            </template>
          </v-simple-table>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false"> I accept </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  props: {
    type: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      currency: [],
      todayCurrency: {},
      dialog: false,
      loading: true,
    }
  },
  async mounted() {
    this.loading = true
    if (this.type === 'USD') {
      this.currency = await this.getCurrencyUSD()
    } else {
      this.currency = await this.getCurrencyUF()
    }
    this.todayCurrency = this.currency.shift()

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

<style scoped>
.bottom-button {
  position: absolute;
  bottom: 10px;
  left: 80px;
  left: 1;
}
</style>
