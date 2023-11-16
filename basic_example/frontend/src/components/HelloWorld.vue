<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ msg: string }>()

const inputText = ref('Fulano');
const resultText = ref('');

const fetchData = async () => {
  try {
    const response = await fetch(`${import.meta.env.VITE_BACKEND_HOST}/api/name/${inputText.value}`);
    const data = await response.json();
    resultText.value = JSON.stringify(data);
  } catch (error) {
    console.error('Erro ao buscar dados da API:', error);
  }
}

</script>

<template>
  <h1>{{ msg }}</h1>

  <div>
    <form @submit.prevent="fetchData">
      <label>
        Digite algo:
        <input v-model="inputText" type="text" />
      </label>
      <button type="submit">Buscar</button>
    </form>
    <div>
      <p>Resultado:</p>
      <textarea rows="4" cols="50" v-model="resultText" readonly></textarea>
    </div>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
