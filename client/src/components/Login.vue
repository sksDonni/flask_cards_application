<template>
    <div>
        <h1> Login </h1>
        <hr />
        <form @submit.prevent @submit="login">
            <div>
                <label>Email</label>
                <input type="text" v-model="values.email" />
            </div>
            <div>
                <label>password</label>
                <input type="password" v-model="values.password" />
            </div>
            <button type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import { mapState } from 'vuex'
export default{
    data(){
        return{
            values:{
                email:'',
                password:'',
            },
        }
    },
    methods:{
        login(){
            let data_submitted = this.values
            this.$store.dispatch("loginUser", data_submitted)
            .then(response => {
                if(response.status == 200){
                    let {data} = response
                    let auth_token = data.response.user.authentication_token
                    localStorage.setItem('auth_token', auth_token)
                    this.$router.push('/')
                }
            })
        }
    },
}
</script>
