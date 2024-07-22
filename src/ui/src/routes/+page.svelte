<script lang="ts">
	import { Badge, Card, Alert } from 'flowbite-svelte';
	import { InfoCircleSolid } from 'flowbite-svelte-icons';
</script>

<div>
	<div class="section">
		<div class="section-content">
			<span>Event Start <Badge border color="primary">00:00:00 Z</Badge></span>
			<span>Time to next State <Badge border color="primary">00:00:00 Z</Badge></span>
			<span>Running Clock <Badge border color="primary">00:00:00 Z</Badge></span>
		</div>
	</div>

	<div class="section-title">State</div>
	<div class="section status">
		<Card class="m-4" color="primary">System Checkout</Card>
		<Card class="m-4" color="primary">Pre-Mission</Card>
		<Card class="m-4" color="primary">Active Trial</Card>
		<Card class="m-4" color="primary">Trial Pause/Delay</Card>
		<Card class="m-4" color="primary">Post-Trial</Card>
		<Card class="m-4" color="primary">Return to Base</Card>
	</div>
	<div class="section status">
		<Card class="m-4 " color="primary">Delay</Card>
	</div>

	<div class="section">
		<Alert class="text-xl">
			<InfoCircleSolid slot="icon" class="h-5 w-5" />
			Delay Reason: [Reason]</Alert
		>
	</div>

	<div class="section">
		<div class="section-title">Speech to Text Transcription</div>
		<div class="mx-auto my-8 flex w-11/12 flex-col">
			<div class="overflow-hidden rounded-lg bg-gray-800 font-mono text-white">
				<div class="h-48 max-h-full overflow-auto p-4">
					<ol class="custom-ol">
						<li>
							<span class="custom-li-content">Alpha: Tango 1, this is Bravo Actual, over.</span>
						</li>
						<li>
							<span class="custom-li-content"
								>Tango 1: Bravo Actual, this is Tango 1, go ahead, over.</span
							>
						</li>
						<li>
							<span class="custom-li-content"
								>Bravo Actual: Tango 1, be advised, enemy forces spotted at grid coordinates 123456,
								over.</span
							>
						</li>
						<li>
							<span class="custom-li-content"
								>Tango 1: Copy that, Bravo Actual. We will proceed with caution, over.</span
							>
						</li>
						<li>
							<span class="custom-li-content">Alpha: Tango 1, this is Bravo Actual, over.</span>
						</li>
						<li>
							<span class="custom-li-content"
								>Tango 1: Bravo Actual, this is Tango 1, go ahead, over.</span
							>
						</li>
						<li>
							<span class="custom-li-content"
								>Bravo Actual: Tango 1, be advised, enemy forces spotted at grid coordinates 123456,
								over.</span
							>
						</li>
						<li>
							<span class="custom-li-content"
								>Tango 1: Copy that, Bravo Actual. We will proceed with caution, over.</span
							>
						</li>
						<li>
							<span class="custom-li-content">Alpha: Tango 1, this is Bravo Actual, over.</span>
						</li>
						<li>
							<span class="custom-li-content"
								>Tango 1: Bravo Actual, this is Tango 1, go ahead, over.</span
							>
						</li>
						<li>
							<span class="custom-li-content"
								>Bravo Actual: Tango 1, be advised, enemy forces spotted at grid coordinates 123456,
								over.</span
							>
						</li>
						<li>
							<span class="custom-li-content"
								>Tango 1: Copy that, Bravo Actual. We will proceed with caution, over.</span
							>
						</li>
						<li>
							<span class="custom-li-content">Alpha: Tango 1, this is Bravo Actual, over.</span>
						</li>
						<li>
							<span class="custom-li-content"
								>Tango 1: Bravo Actual, this is Tango 1, go ahead, over.</span
							>
						</li>
						<li>
							<span class="custom-li-content"
								>Bravo Actual: Tango 1, be advised, enemy forces spotted at grid coordinates 123456,
								over.</span
							>
						</li>
						<li>
							<span class="custom-li-content"
								>Tango 1: Copy that, Bravo Actual. We will proceed with caution, over.</span
							>
						</li>
					</ol>
				</div>
			</div>
		</div>
	</div>

	<div class="section">
		<div class="section-title">Performance Metrics</div>
		<div class="section-content">[What is most important to the user?]</div>
	</div>
</div>

<style>
	.status {
		text-align: center;
		justify-content: center;
	}
	.section {
		display: flex;
	}
	.custom-ol {
		counter-reset: custom-counter;
		list-style: none; /* Removes default list styling */
		padding-left: 0; /* Adjusts padding */
	}
	.custom-ol li {
		counter-increment: custom-counter;
		margin-bottom: 8px; /* Adjusts space between items */
	}
	.custom-ol li::before {
		content: counter(custom-counter) ' ';
		font-weight: bold; /* Makes the counter bold */
		margin-right: 8px; /* Adjusts space between the counter and the text */
	}
	.custom-li-content {
		display: inline-block;
		max-width: calc(100% - 30px); /* Adjusts max width to prevent overlap with the counter */
		vertical-align: top; /* Aligns content at the top */
	}

</style>
