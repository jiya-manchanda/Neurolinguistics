# Concept Acquisition in Humans and Large Language Models

I hope to explore the process of concept acquisition in humans and critically evaluate whether connectionist artificial intelligence systems, specifically large language models (LLMs), can acquire abstract concepts in a manner akin to human cognition (Cherkassky & Lee, 2024). Specifically, my focus will be the neuroscience underlying language production (Xing et al., 2018), in light of the problem of abstraction within the empiricist framework of epistemology (Spelke, 1998). Abstraction is central to the human capacity to form complex ideas and conceptual structures, enabling higher-order cognition and nuanced understanding (Laurence & Margolis, 2012). Given that concepts are foundational to language (McDonald & MacWhinney, 1991), my question is: can LLMs, despite their sophisticated capacity to produce language, possess "linguistic" competence in principle? Or, is it the case that they are fundamentally constrained due to a lack of concept acquisition abilities?

## Research Question
Can connectionist artificial intelligence systems, specifically large language models (LLMs), acquire abstract concepts in a manner akin to human cognition, or are they constrained by their reliance on pattern recognition?

## Final Project Format
The final project will take the form of a Python-coded simulation that models and contrasts the cognitive processes of humans and LLMs in concept formation and linguistic competence. My program will consist of two primary classes:

1. **Human Cognition Class**: In this class, I will simulate how humans acquire and use abstract concepts, integrating sensory inputs, introspection, and situational context. Functions like `perceive()` will model how sensory data is processed, while methods like `generate_output()` will simulate how humans draw on these data to produce abstract ideas. Additional methods might include `combine_concepts()` or `reflect()`, representing processes like conceptual synthesis and introspection.

2. **AI Model Class**: In this class, I will simulate an LLM’s operation, including its reliance on training data, pattern recognition, and statistical inference. Functions such as `parse_data()` and `generate_output()` will highlight how an LLM processes input and generates responses, showcasing its lack of grounding in sensory or introspective experiences.

The program will allow user input of concepts (e.g., “truth” or “freedom”), providing a comparative visualization or textual explanation of how humans and AI would process these ideas. Accompanying the code, detailed comments will analyze the results, connecting them to relevant philosophical and psychological theories, such as empiricism, nativism, and theories of abstraction. These comments will serve as the equivalent of a research paper’s body, providing context, interpretation, and critique.

## Progress Report
So far, I have made significant progress in narrowing down my research question and gathering sources to build a strong theoretical foundation. My progress thus far has focused on bridging the philosophical and computational dimensions of the research question, the former honing in on key theories of abstraction, such as Barsalou’s situational grounding and Spelke’s nativist framework, to frame human cognition, while leveraging critiques of LLMs’ statistical methodologies from sources like Marcus and Cherkassky. This interdisciplinary foundation has helped clarify the stark differences between human and AI conceptualization.

On the technical side, I have outlined the structural framework for the Python simulation and drafted the foundational methods for the two primary classes. However, challenges remain. Translating abstract cognitive processes into functional code demands careful calibration to avoid oversimplification while maintaining computational feasibility. The nuances of introspection and situational grounding, in particular, are proving difficult to encapsulate algorithmically. Additionally, balancing the depth of philosophical engagement with the technical robustness of the simulation continues to require deliberate effort.

Moving forward, I aim to focus on the following priorities to ensure the project is both theoretically insightful and technically sound:

1. Finalizing the coding framework for the human cognition and AI model classes.
2. Developing comprehensive use cases for user inputs that effectively demonstrate the divergences between human and AI processing.
3. Expanding my written analysis to ensure it seamlessly integrates the simulation’s results with insights from the philosophical and psychological literature.

## Annotated Bibliography

Barsalou, L. W., & Wiemer-Hastings, K. (2005). Situating abstract concepts. *Cambridge University Press, 129–163*. https://doi.org/10.1017/cbo9780511499968.007. 
Summary: Barsalou and Wiemer-Hastings argue that abstract concepts are dynamically grounded in situational and introspective contexts. They contrast abstract concepts, which rely heavily on situational variability, with concrete concepts, which exhibit stronger sensory grounding.
Assessment: This source provides a critical foundation for articulating the situational and introspective elements of human abstraction. It highlights the absence of such grounding in LLMs and will serve as a cornerstone for critiquing AI’s inability to simulate conceptual context.

Borghi, A. M., Barca, L., Binkofski, F., & Tummolini, L. (2018). Abstract concepts, language and sociality: from acquisition to inner speech. *Philosophical Transactions of the Royal Society B Biological Sciences, 373*(1752), 20170134. https://doi.org/10.1098/rstb.2017.0134.
Summary: Borghi et al. argue that abstract concepts rely heavily on language and social interactions for acquisition and internalization. They highlight the role of inner speech in managing and integrating these concepts.
Assessment: This source will be used to illustrate the fundamentally social nature of abstract concept formation in humans, contrasting it with the isolated statistical models used in LLMs.

Carey, S. (2011). Précis of *The Origin of Concepts*. *Behavioral and Brain Sciences, 34*(3), 113–124. https://doi.org/10.1017/s0140525x10000919.
Summary: Carey presents a hybrid model of concept acquisition, arguing that it combines innate structures with empirical experiences. The paper focuses on how humans generate novel abstract ideas through hierarchical learning.
Assessment: This source provides theoretical grounding for the nativist perspective in my project, which I will contrast with AI’s reliance on preprocessed data and lack of innate structures.

Cherkassky, V., & Lee, E. H. (2024). A perspective on large language models, intelligent machines, and knowledge acquisition. *arXiv (Cornell University)*. https://doi.org/10.48550/arxiv.2408.06598.
Summary: This paper critiques LLMs’ epistemic abilities, emphasizing their inability to form true concepts due to reliance on pattern recognition. Cherkassy et al. propose that LLMs generate only a superficial mimicry of human knowledge.
Assessment: This is a cornerstone source for arguing that LLMs lack true abstraction, as their “knowledge” is entirely statistical and devoid of conceptual grounding.

Chiou, R., & Ralph, M. a. L. (2019). Unveiling the dynamic interplay between the hub- and spoke-components of the brain’s semantic system and its impact on human behaviour. *NeuroImage, 199*, 114–126. https://doi.org/10.1016/j.neuroimage.2019.05.059. 
Summary: This paper explores the neural mechanisms underlying the human semantic system, focusing on the interaction between the “hub” (anterior temporal lobe) and “spoke” (sensory-motor regions) components. Chiou et al. argue that this dynamic interplay enables the integration of diverse inputs into coherent semantic representations.
Assessment: This source will be instrumental in illustrating how human cognition integrates multimodal sensory data to form abstract concepts. It will also support the argument that human semantic processing relies on a highly interactive neural network, whereas AI models are constrained by static, ungrounded data representations.

Constantinescu, I., Pimentel, T., Cotterell, R., & Warstadt, A. (2024). Do language models have a critical period for language acquisition? *arXiv (Cornell University)*. https://doi.org/10.48550/arxiv.2407.19325.
Summary: This study investigates whether LLMs mimic humans’ critical period for language acquisition, finding that LLMs exhibit no such developmental constraints.
Assessment: This source will support the argument that LLMs, unlike humans, do not undergo a developmental trajectory, reinforcing their fundamental differences from human cognitive processes.

Lake, B. M., Ullman, T. D., Tenenbaum, J. B., & Gershman, S. J. (2016). Building machines that learn and think like people. *Behavioral and Brain Sciences, 40*. https://doi.org/10.1017/s0140525x16001837. 
Summary: This paper outlines principles for developing AI systems that emulate human cognitive processes, emphasizing learning from small data, compositionality, causality, and grounded understanding. Lake et al. argue that current machine learning systems, including LLMs, fail to replicate the flexibility and conceptual depth of human thought. They propose a shift toward incorporating structured cognitive models to achieve human-like AI.
Assessment: This source will provide critical insights into the limitations of LLMs, specifically their reliance on large datasets and lack of causal reasoning. It will be used to argue for the fundamental differences between human conceptual learning and AI pattern recognition, supporting the position that LLMs do not achieve true abstraction.

Laurence, S., & Margolis, E. (2012). Abstraction and the origin of general ideas. *Philosopher’s Imprint, 12*(19), 1–22. https://quod.lib.umich.edu/cgi/p/pod/dod-idx/abstraction-and-the-origin-of-general-ideas.pdf?c=phimp;idno=3521354.0012.019;format=pdf. 
Summary: Laurence and Margolis analyze how abstraction enables the formation of general ideas, emphasizing cognitive mechanisms that allow humans to go beyond sensory experiences.
Assessment: This will be used to show that human abstraction processes are fundamentally different from LLMs, which cannot generalize beyond data patterns.

Magid, R. W., Sheskin, M., & Schulz, L. E. (2015). Imagination and the Generation of New Ideas. *Cognitive Development, 34*, 99–110. https://doi.org/10.1016/j.cogdev.2014.12.008.
Summary: This article explores the role of imagination in the creation of new ideas and concepts, particularly in childhood development.
Assessment: I will use this to argue that imagination, a key component of human cognition, is entirely absent in LLMs.

MacDonald, B., & Witten, I. (1989). A framework for knowledge acquisition through techniques of concept learning. *IEEE Transactions on Systems Man and Cybernetics, 19*(3), 499–512. https://doi.org/10.1109/21.31057.
Summary: MacDonald et al. present methods for concept learning in AI systems, emphasizing algorithmic approaches and their limitations in replicating human conceptual understanding.
Assessment: This will provide context for historical challenges in AI’s attempts to replicate human-like knowledge acquisition.

Marcus, G. (2018). Innateness, AlphaZero, and artificial intelligence. *arXiv (Cornell University)*. https://doi.org/10.48550/arxiv.1801.05667. 
Summary: Marcus critiques modern AI systems, arguing that they lack the innate scaffolding present in human cognition. He highlights the limitations of deep learning models, such as AlphaZero, in understanding abstract principles and posits that integrating innate structures into AI design could enhance their capabilities. The paper contrasts AI’s reliance on statistical pattern recognition with the innate, flexible reasoning humans use to form abstract concepts.
Assessment: This source will bolster arguments about the necessity of innate structures for abstract thought, positioning human cognition as fundamentally different from AI systems. It will also support critiques of the empiricist approach in current AI, aligning with philosophical arguments about the limitations of antecedently supplied labelled training datasets categorized according to various grouping principles.

McDonald, J. L., & MacWhinney, B. (1991). Levels of learning: A comparison of concept formation and language acquisition. *Journal of Memory and Language, 30*(4), 407–430. https://doi.org/10.1016/0749-596x(91)90014-b.
Summary: The article emphasizes hierarchical learning, comparing how humans form concepts and acquire language in structured stages.
Assessment: This will support my argument that humans progress through learning stages, unlike LLMs, which do not evolve over time.

Miller, S., Jungheim, M., & Ptok, M. (2014). Erstspracherwerbsforschung und Spracherwerbstheorien. *HNO, 62*(4), 242–248. https://doi.org/10.1007/s00106-014-2855-z.
Summary: This paper discusses theories of first language acquisition, including nativist, empiricist, and interactionist perspectives.
Assessment: It will provide comparative insights into how language acquisition theories differ from the mechanisms employed by LLMs.

Rohlfing, K. J., Wrede, B., Vollmer, A., & Oudeyer, P. (2016). An Alternative to Mapping a Word onto a Concept in Language Acquisition: Pragmatic Frames. *Frontiers in Psychology, 7*. https://doi.org/10.3389/fpsyg.2016.00470.
Summary: This paper introduces pragmatic frames, arguing that social and situational contexts are crucial for word-to-concept mapping.
Assessment: This will highlight the limitations of LLMs, which lack access to pragmatic and social contexts.

Schulz, L. (2012). The origins of inquiry: inductive inference and exploration in early childhood. *Trends in Cognitive Sciences, 16*(7), 382–389. https://doi.org/10.1016/j.tics.2012.06.004. 
Summary: Schulz discusses how children use exploration and inductive reasoning to generate new ideas, emphasizing active learning processes.
Assessment: This supports the argument that human learning is dynamic and exploratory, contrasting with the static nature of LLM training.

Spelke, E. S. (1998). Nativism, empiricism, and the origins of knowledge. *Infant Behavior and Development, 21*(2), 181–200. http://harvardlds.org/wp-content/uploads/2017/01/spelke1998-1.pdf. 
Summary: Spelke advocates for a nativist view, proposing that humans possess innate structures that guide early knowledge formation.
Assessment: This will contrast human nativist capacities with the data-driven empiricism of LLMs.

Wei, H. (2020). The evolution of concept-acquisition based on developmental psychology. *arXiv (Cornell University)*. https://doi.org/10.48550/arxiv.2011.13089.
Summary: This paper outlines developmental trajectories in concept acquisition, focusing on how abstraction evolves over time.
Assessment: It will emphasize the absence of temporal evolution in LLM learning processes.

Witten, I. H., & MacDonald, B. A. (1988). Using concept learning for knowledge acquisition. *International Journal of Man-Machine Studies, 29*(2), 171–196. https://doi.org/10.1016/s0020-7373(88)80045-2.
Summary: Witten et al. critique early AI approaches to concept learning, noting their reliance on rigid algorithms.
Assessment: This will provide historical context for the limitations of computational models in replicating human cognition.

Xing, Y., Shi, X., Shen, F., Zhao, J., Pan, J., & Tan, A. (2018). Perception Coordination Network: a neuro framework for multimodal concept acquisition and binding. *IEEE Transactions on Neural Networks and Learning Systems, 30*(4), 1104–1122. https://doi.org/10.1109/tnnls.2018.2861680.
Summary: This paper presents a neural framework for integrating sensory modalities to form concepts.
Assessment: I will use this to contrast multimodal integration in human cognition with the unimodal data processing of LLMs.
