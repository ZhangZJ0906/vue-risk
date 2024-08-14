<template>
    <div>
        <h1>風險結果</h1>
        <div v-if="moeaData">
            <h2>公司資訊</h2>
            <p>公司名稱: {{ moeaData.CompanyName }}</p>
            <p>公司狀態: {{ moeaData.CompanyStatusDesc }}</p>
            <p>資本總額: {{ moeaData.CapitalStockAmount }}</p>
            <p>負責人: {{ moeaData.ResponsibleName }}</p>
            <p>公司地址: {{ moeaData.CompanyLocation }}</p>
        </div>

        <div v-if="prtrData && prtrData.NumberOfData">
            <h2>裁處資訊</h2>
            <p>{{ prtrData.NumberOfData }}</p>
        </div>

        <div v-if="ppstrqData">
            <h2>擔保資料</h2>
            <p>登記機關: {{ ppstrqData.RegistrationAuthority }}</p>
            <p>案件類別: {{ ppstrqData.CaseCategory }}</p>
            <p>抵押人名稱: {{ ppstrqData.DebtorName }}</p>
            <p>抵押權人名稱: {{ ppstrqData.NameOfMortgagee }}</p>
            <p>案件狀態: {{ ppstrqData.CaseStatus }}</p>
        </div>

        <div v-if="twincnData">
            <h2>統編資料</h2>
            <p>公司名稱: {{ twincnData.CompanyName }}</p>
            <p>訴訟狀態: {{ twincnData.Lawsuit }}</p>
            <p>營業狀態: {{ twincnData.state }}</p>
            <p>是否開統一發票: {{ twincnData.Use_unified_invoice }}</p>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';

export default {
    setup() {
        const moeaData = ref(null);
        const prtrData = ref(null);
        const ppstrqData = ref(null);
        const twincnData = ref(null);

        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost/STU-Topics/backend/getdata.php', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                // 先獲取原始文本以進行調試
                const text = await response.text();
                console.log('Raw response:', text);

                // 嘗試解析 JSON
                const data = JSON.parse(text);

                console.log('Parsed data:', data);

                moeaData.value = data.py_moea_input[0];
                prtrData.value = data.py_prtr_input[0];
                ppstrqData.value = data.py_ppstrq_input[0];
                twincnData.value = data.twincn[0];
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        onMounted(() => {
            fetchData();
        });

        return {
            moeaData,
            prtrData,
            ppstrqData,
            twincnData
        };
    }
};
</script>
