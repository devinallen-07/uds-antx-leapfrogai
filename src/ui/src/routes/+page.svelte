<script lang="ts">
	import ClocksCard from '$lib/components/cards/ClocksCard.svelte';
	import StateCard from '$lib/components/cards/StateCard.svelte';
	import Transcript from '$lib/components/cards/Transcript.svelte';
	import SpeechToTextCard from '$lib/components/cards/Transcript.svelte';

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

<div>
	<ClocksCard {testimonials} />
	<StateCard list={states} />
	<StateCard list={delayStates} />
	<Transcript list={dummyTranscript} />

	<div class="section">
		<div class="section-title">Performance Metrics</div>
		<div class="section-content">[What is most important to the user?]</div>
	</div>
</div>
