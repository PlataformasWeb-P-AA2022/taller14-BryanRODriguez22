<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="costo">Costo Departamento</label>
                <input
                    type="number"
                    class="form-control"
                    id="costo"
                    v-model="departamento.costo_depa"
                    v-validate="'required'"
                    name="costo"
                    placeholder="Ingrese el valor del departamento"
                    :class="{'is-invalid': errors.has('departamento.costo_depa') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid costo.
                </div>
            </div>

            <div class="form-group">
                <label for="cuartos">Numero de cuartos</label>
                <input
                    type="number"
                    class="form-control"
                    id="cuartos"
                    v-model="departamento.num_cuartos"
                    v-validate="'required'"
                    name="cuartos"
                    placeholder="Ingrese el numero de cuartos"
                    :class="{'is-invalid': errors.has('departamento.num_cuartos') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero cuartos.
                </div>
            </div>

            <div class="form-group">
                <label for="banio">Numero de baños</label>
                <input
                    type="number"
                    class="form-control"
                    id="banio"
                    v-model="departamento.num_banio"
                    v-validate="'required'"
                    name="banio"
                    placeholder="Ingrese el numero de baños"
                    :class="{'is-invalid': errors.has('departamento.num_banio') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid numero baños.
                </div>
            </div>

            <div class="form-group">
                <label for="alicuota">Valor de alicuota</label>
                <input
                    type="number"
                    class="form-control"
                    id="alicuota"
                    v-model="departamento.alicuota"
                    v-validate="'required'"
                    name="alicuota"
                    placeholder="Ingrese el valor de la alicuota"
                    :class="{'is-invalid': errors.has('departamento.alicuota') && submitted}">
                <div class="invalid-feedback">
                    Please provide a valid alicuota.
                </div>
            </div>
            <div class="form-group">
              <br>
                <label for="propietario">Propietario</label>
                <select v-model="departamento.propietario">
                            <option v-for="e in propietarioList" :key="e.url" :value="e.url">{{ e.nombre }} {{ e.apellido }}</option>
                        </select>
            </div>
            <br>
            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            departamento: {
                costo_depa: '',
                num_cuartos: '',
                num_banio: '',
                alicuota: '',
                propietario: '',
            },
            propietarioList: [],
            submitted: false
        }
    },
    mounted() {
        this.getPropietariosList(),
        axios.get('http://127.0.0.1:8000/api/departame/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.telefono = response.data
        });
    },
    methods: {
      getPropietariosList() {
            axios
            .get('http://127.0.0.1:8000/api/propietario/')
            .then(response => {
                this.estudiantesList = response.data
            })
            .catch(error => {
                console.log(error)
            })

        },
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://127.0.0.1:8000/api/departame/${this.telefono.id}/`,
                        this.telefono
                    )
                    .then(response => {
                        this.$router.push('/departamentos');
                    })
            });
        }
    },
}
</script>
