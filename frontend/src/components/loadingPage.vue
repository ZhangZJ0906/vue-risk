<template>
    loadign 中..

</template>

<script>
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const router = useRouter();

        const checkFile = async () => {
            const checkFileInterval = setInterval(async () => {
                try {
                    const response = await axios.get('http://localhost/STU-Topics/backend/check_json.php');
                    if (response.status === 200) {
                        clearInterval(checkFileInterval);
                        // 跳转到结果页面
                        router.push({ name: 'RiskResultPage' });
                    }
                } catch (error) {
                    console.error("Error checking file:", error);
                }
            }, 2000); // 每2秒检查一次
        };


        return {
            checkFile,
        };
    },
    mounted() {
        this.checkFile();
    }
};
</script>