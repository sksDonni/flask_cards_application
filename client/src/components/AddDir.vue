<template>
    <div>
        <h1> Add Directory </h1>
        <hr />
        <form @submit.prevent @submit="add_dir" class="main-form">
            <div>
                <label>Directory Name</label>
                <input type="text" v-model="values.dir_name" />
            </div>
            <button class="main-button" type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default{
    data(){
        return{
            values:{
                dir_name:'',
            },
        }
    },
    methods:{
        add_dir(){
            let data_submitted = { ...this.values}
            console.log(data_submitted)
            this.$store.dispatch("addDir", data_submitted)
            .then(res => {
                if(res.status == 200){
                    this.$router.push('/')
                }
            })
        }
    },
    computed:{
        ...mapState({
            dir_id: state => state.individualDeck.dir_id,
        }),
    },
    mounted(){

    }
}
</script>
