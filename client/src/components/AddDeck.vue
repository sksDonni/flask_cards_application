<template>
    <div>
        <h1> Add Decks </h1>
        <hr />
        <form @submit.prevent @submit="add_deck" class="main-form">
            <div>
                <label>Name</label>
                <input type="text" v-model="values.deck_name" />
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
                deck_name:'',
            },
        }
    },
    methods:{
        add_deck(){
            let dir_id = this.dir_id
            console.log(dir_id)
            let data_submitted = { ...this.values, dir_id}
            console.log(data_submitted)
            this.$store.dispatch("addDeckByDir", data_submitted)
            .then(res => {
                if(res.status == 200){
                    this.$router.push(`/directory/${this.dir_id}`)
                }
            })
        }
    },
    computed:{
        ...mapState({
            dir_id: state => state.individualDir.dir_id,
        }),
    },
    mounted(){
        let id = this.$route.params.id
        this.$store.dispatch("fetchDirectoryById", {id})
    }
}
</script>
