<template>
    <div class="mainContent">
        <el-tabs type="border-card" :stretch="true" model-value="Login" class="authCard">
            <el-tab-pane label="Login" name="Login" >
                <LoginCard/>
            </el-tab-pane>
            <el-tab-pane label="Sign Up" name="Sign Up">
                <SignUpCard/>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
import LoginCard from "@/components/AuthCards/LoginCard";
import SignUpCard from "@/components/AuthCards/SignUpCard";
import { ElTabs } from 'element-plus';

export default {
    components: {
        LoginCard,
        SignUpCard,
        ElTabs
    },
    setup() {

    }
}
</script>

<style>
.authCard {
    max-width: 30%;
    max-height: fit-content;
    margin: auto auto;
}
</style>