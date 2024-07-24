<script lang="ts">
	import ClocksCard from '$lib/components/cards/ClocksCard.svelte';
	import StateCard from '$lib/components/cards/StateCard.svelte';
	import SpeechToTextCard from '$lib/components/cards/SpeechToTextCard.svelte';

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
</script>

<div>
	<ClocksCard {testimonials} />
	<StateCard list={states} />
	<StateCard list={delayStates} />
	<SpeechToTextCard />

	<div class="section">
		<div class="section-title">Performance Metrics</div>
		<div class="section-content">[What is most important to the user?]</div>
	</div>
</div>
