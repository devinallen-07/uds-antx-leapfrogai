<script lang="ts">
	import ClocksCard from '$lib/components/cards/ClocksCard.svelte';
	import StateCard from '$lib/components/cards/StateCard.svelte';
	import Transcript from '$lib/components/cards/Transcript.svelte';
	import PerformanceCard from '$lib/components/cards/PerformanceCard.svelte';
	import { Accordion, AccordionItem, Button } from 'flowbite-svelte';
	import { Api } from '$lib/api';

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

	const states = ['Pre Trial Start', 'Trial Start', 'In Transit', 'Mistrial', 'RTB', 'Trial End'];

	const delayStates = ['Delay Start', 'Delay End'];

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
	<Button class="m-2 mt-8 dark:bg-gray-700 border" color="primary" size="lg" on:click={Api.start}>Start</Button>
	<Button class="m-2 mt-8 dark:bg-gray-700 border" color="primary" size="lg" on:click={Api.update}>Update</Button>
	<Button class="m-2 mt-8 dark:bg-gray-700 border" color="primary" size="lg" on:click={Api.end}>End</Button>
</div>
