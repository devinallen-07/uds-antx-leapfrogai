<script lang="ts">
	import ClocksCard from '$lib/components/cards/ClocksCard.svelte';
	import StateCard from '$lib/components/cards/StateCard.svelte';
	import Transcript from '$lib/components/cards/Transcript.svelte';
	import PerformanceCard from '$lib/components/cards/PerformanceCard.svelte';
	import { Accordion, AccordionItem, Button } from 'flowbite-svelte';
	import { Api } from '$lib/api';
	import { updateEventStore } from '../stores/stateStore';

	const testimonials = [
		{
			title1: 'Event Start',
			title2: '00:00:00 Z'
		},
		{
			title1: 'Time to next State',
			title2: '00:00:00 Z'
		},
		{
			title1: 'Running Clock',
			title2: '00:00:00 Z'
		}
	];

	const states = [
		{ name: 'Pre Trial Start', isCurrent: true },
		{ name: 'Trial Start', isCurrent: false },
		{ name: 'In Transit', isCurrent: false },
		{ name: 'Mistrial', isCurrent: false },
		{ name: 'Trial End', isCurrent: false },
		{ name: 'RTB', isCurrent: false }
	];

	const delayStates = [
		{ name: 'Delay Start', isCurrent: false },
		{ name: 'Delay End', isCurrent: false }
	];

	const dummyTranscript = [
		'Alpha: Tango 1, this is Bravo Actual, over.',
		'Tango 1: Bravo Actual, this is Tango 1, go ahead, over.',
		'Bravo Actual: Tango 1, be advised, enemy forces spotted at grid coordinates 123456, over.',
		'Tango 1: Copy that, Bravo Actual. We will proceed with caution, over.',
		'Alpha: Tango 1, this is Bravo Actual, over.',
		'Tango 1: Bravo Actual, this is Tango 1, go ahead, over.',
		'Bravo Actual: Tango 1, be advised, enemy forces spotted at grid coordinates 123456, over.',
		'Tango 1: Copy that, Bravo Actual. We will proceed with caution, over.',
		'Alpha: Tango 1, this is Bravo Actual, over.',
		'Tango 1: Bravo Actual, this is Tango 1, go ahead, over.',
		'Bravo Actual: Tango 1, be advised, enemy forces spotted at grid coordinates 123456, over.',
		'Tango 1: Copy that, Bravo Actual. We will proceed with caution, over.',
		'Alpha: Tango 1, this is Bravo Actual, over.',
		'Tango 1: Bravo Actual, this is Tango 1, go ahead, over.',
		'Bravo Actual: Tango 1, be advised, enemy forces spotted at grid coordinates 123456, over.',
		'Tango 1: Copy that, Bravo Actual. We will proceed with caution, over.',
		'short line'
	];

	async function fetchUpdate() {
		const newData = await Api.update();
		updateEventStore(newData);
	}
</script>

<ClocksCard {testimonials} />
<StateCard list={states} />
<StateCard list={delayStates} />

<Accordion multiple class="mx-auto w-5/6">
	<AccordionItem open>
		<span slot="header">Transcript</span>
		<Transcript list={dummyTranscript} />
	</AccordionItem>
	<AccordionItem open>
		<span slot="header">Performance Metrics</span>
		<PerformanceCard />
	</AccordionItem>
</Accordion>

<div class="flex justify-center">
	<Button class="m-2 mt-8 border dark:bg-gray-700" color="primary" size="lg" on:click={Api.start}
		>Start</Button
	>
	<Button class="m-2 mt-8 border dark:bg-gray-700" color="primary" size="lg" on:click={fetchUpdate}
		>Update</Button
	>
	<Button class="m-2 mt-8 border dark:bg-gray-700" color="primary" size="lg" on:click={Api.end}
		>End</Button
	>
</div>
