<script lang="ts">
	import ClocksCard from '$lib/components/cards/ClocksCard.svelte';
	import StateCard from '$lib/components/cards/StateCard.svelte';
	import Transcript from '$lib/components/cards/Transcript.svelte';
	import PerformanceCard from '$lib/components/cards/PerformanceCard.svelte';
	import { Accordion, AccordionItem } from 'flowbite-svelte';
	import { Api } from '$lib/api';
	import { updateEventStore } from '../stores/stateStore';

	async function fetchUpdate() {
        try {
            const response = await Api.update();
            if (response.error) {
                console.error('Error fetching update:', response.error);
            } else if (response.data) {
                updateEventStore(response.data);
            }
        } catch (error) {
            console.error('Unexpected error during update:', error);
        }
    }

	function startUpdateInterval() {
		setInterval(fetchUpdate, 3000);
	}

	startUpdateInterval();
</script>

<ClocksCard />
<StateCard />

<Accordion multiple class="mx-auto w-5/6">
	<AccordionItem closed>
		<span slot="header">Transcript</span>
		<Transcript />
	</AccordionItem>
	<AccordionItem closed>
		<span slot="header">Performance Metrics</span>
		<PerformanceCard />
	</AccordionItem>
</Accordion>
