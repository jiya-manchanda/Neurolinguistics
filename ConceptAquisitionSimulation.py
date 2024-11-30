import networkx as nx
import matplotlib.pyplot as plt

# Define Human Cognition Class
class HumanCognition:
    """
    A class to simulate human cognition in concept acquisition and abstraction.
    This class models how humans use sensory inputs, memory, emotions, and situational context
    to acquire and form concepts.
    """
    def __init__(self, concept):
        # Referencing Barsalou & Wiemer-Hastings (2005), abstract concepts are grounded in
        # situational contexts. Human cognition is context-dependent; abstract concepts such
        # as 'freedom' rely heavily on the cultural, situational, and introspective contexts
        # in which they are experienced. This dynamic grounding contrasts sharply with the static
        # representation mechanisms found in AI, where concepts are purely data-driven and lack
        # an experiential base.
        self.concept = concept
        self.sensory_inputs = self.get_sensory_inputs(concept)
        self.innate_structure = self.get_innate_structure(concept)
        # Situational context is a critical aspect of concept formation (Barsalou &
        # Wiemer-Hastings, 2005). In human cognition, situational context acts as a scaffold
        # for constructing meaning, integrating social, cultural, and environmental cues to
        # form a coherent representation of abstract ideas. This stands in contrast to AI systems,
        # which do not integrate contextual variance dynamically.
        self.situational_context = f"Cultural and social environment specific to '{concept}'"
        # Memory retrieval based on past experiences aligns with Carey (2011)'s hybrid model
        # of concept acquisition. Carey (2011) proposes a hybrid model of concept acquisition
        # that involves both innate cognitive structures and empirical experiences. This reflects
        # the idea that human cognition is influenced by a combination of biological predispositions
        # (e.g., neural circuits related to moral reasoning) and accumulated experiences, creating
        # a hierarchical process for acquiring new concepts.
        self.memory = f"Past experiences and knowledge related to '{concept}'"
        # Integration of emotions is important for human concept acquisition, as argued by
        # Borghi et al. (2018). Borghi et al. (2018) argue that emotions are integral to the
        # formation and management of abstract concepts. Emotions are not merely by-products of
        # cognition but serve a regulatory role, affecting how concepts are internalized,
        # recalled, and applied in new contexts. This aspect of emotional integration is absent
        # in AI systems, which simulate emotions through sentiment analysis but lack the
        # phenomenological experience.
        self.emotions = self.integrate_emotions(concept)

    def get_sensory_inputs(self, concept):
        """
        Retrieve sensory inputs specific to a concept.
        :param concept: str, the concept being acquired
        :return: list of sensory inputs related to the concept
        """
        # Chiou & Ralph (2019) discuss how sensory inputs are integrated into coherent semantic
        # representations. According to Chiou & Ralph (2019), the human semantic system relies
        # on the dynamic interplay between hub (e.g., anterior temporal lobe) and spoke
        # (e.g., sensory-motor regions) components to form coherent semantic representations.
        # Sensory inputs such as visual, auditory, and tactile information are not processed in
        # isolation but are integrated to construct meaningful concepts. This is especially
        # significant for grounding abstract ideas in concrete sensory experiences, enabling
        # humans to connect otherwise intangible concepts to real-world stimuli.
        sensory_inputs_dict = {
            "freedom": ["Sigh of relief", "Picture of Statue of Liberty", "Feeling of open space"],
            "knowledge": ["Reading books", "Listening to lectures", "Analyzing data"],
            "love": ["Seeing a loved one", "Hearing affectionate words", "Feeling a warm hug"],
            "fear": ["Seeing a dangerous animal", "Hearing a loud noise", "Feeling of a fast heartbeat"],
            "success": ["Standing ovation", "Certificates of achievement", "Hearing applause"],
            "failure": ["Seeing a red 'X' mark", "Hearing disappointing news", "Feeling tired"],
            "justice": ["Courtroom visuals", "Hearing the judge's verdict", "Witnessing fairness"],
            "creativity": ["Colors in an artwork", "Musical notes", "Feeling inspired"],
            "trust": ["Handshake", "Seeing a familiar face", "Hearing reassuring words"],
            "change": ["Leaves falling from trees", "Hearing new ideas", "Feeling uncertain"]
        }
        return sensory_inputs_dict.get(concept, ["General sensory input for concept acquisition"])

    def get_innate_structure(self, concept):
        """
        Retrieve innate neural structures related to a concept.
        :param concept: str, the concept being acquired
        :return: str, description of neural activation related to the concept
        """
        # Carey (2011) and Spelke (1998) discuss innate structures in human cognition, which form
        # part of concept acquisition. Carey (2011) emphasizes that concept acquisition in humans is
        # not purely empirical; there are innate structures that shape how new information is
        # interpreted. For instance, Spelke (1998) highlights the nativist perspective, which
        # posits that infants are born with core cognitive capacities that allow them to make
        # sense of their environment. These innate neural structures, such as those involved in
        # processing social cues or recognizing fairness, provide a foundational scaffold that
        # facilitates the development of more complex abstract ideas as individuals interact
        # with their surroundings.
        innate_structure_dict = {
            "freedom": "Neurons associated with positive emotions and stress relief fire when experiencing freedom.",
            "knowledge": "Neurons in the prefrontal cortex activate to process and store new information.",
            "love": "Oxytocin release and activation of reward-related neurons in the brain.",
            "fear": "Activation of the amygdala, triggering the fight-or-flight response.",
            "success": "Dopamine release and reward circuitry activation when achieving success.",
            "failure": "Activation of error-monitoring neurons in the anterior cingulate cortex.",
            "justice": "Activation of moral reasoning areas in the prefrontal cortex.",
            "creativity": "Activation of the default mode network associated with idea generation.",
            "trust": "Neurons related to social bonding and oxytocin release are activated.",
            "change": "Activation of neurons in the prefrontal cortex to adapt to new situations."
        }
        return innate_structure_dict.get(concept, "General neural response for concept acquisition")

    def acquire_concept(self, category):
        """
        Simulate the human concept acquisition process based on a given category.
        :param category: str, the category of concept acquisition (e.g., sensory processing, memory retrieval)
        :return: str, detailed explanation of the human acquisition of the concept
        """
        if category == "sensory processing":
            return f"Human acquisition of '{self.concept}':\nSensory Inputs: {', '.join(self.sensory_inputs)}"
        elif category == "context interpretation":
            # Barsalou & Wiemer-Hastings (2005) emphasize the role of context in abstract
            # concept acquisition. Contextual cues play a pivotal role in grounding abstract
            # concepts, making them relatable and meaningful within specific situations. Unlike
            # purely data-driven systems, humans constantly reinterpret abstract ideas based
            # on evolving situational factors, allowing for flexible and adaptive thinking.
            return f"Human acquisition of '{self.concept}':\nSituational Context: {self.situational_context}"
        elif category == "memory retrieval":
            # Memory retrieval aligns with Carey's (2011) hierarchical learning approach. 
            # Memory retrieval is a key mechanism in human cognition for integrating past
            # experiences into present learning. This hierarchical integration supports the
            # construction of abstract representations by continuously adding layers
            # of meaning based on new contexts and experiences.
            return f"Human acquisition of '{self.concept}':\nMemory Retrieval: {self.memory}"
        elif category == "reinforcement learning":
            # Reinforcement learning is influenced by innate structures, as discussed by
            # Carey (2011) and Marcus (2018). Human learning involves a combination of innate
            # scaffolding and reinforcement learning, where innate predispositions guide the
            # initial stages of learning and reinforcement (e.g., emotional or social rewards)
            # shapes subsequent behavior.
            return f"Human acquisition of '{self.concept}':\nInnate Structure: {self.innate_structure}"
        elif category == "emotional integration":
            # Emotional responses play a crucial role in concept acquisition (Borghi et al., 2018)
            # Emotions are not just responses but are integral in modulating cognitive processes,
            # enabling the internalization of abstract concepts in a way that is intrinsically
            # meaningful to the individual.
            return f"Human acquisition of '{self.concept}':\nEmotional Integration: {self.emotions}"
        else:
            return "Invalid category."

    def integrate_emotions(self, concept):
        """
        Integrate emotional responses related to the concept.
        :param concept: str, the concept being acquired
        :return: str, emotional responses related to the concept
        """
        # Borghi et al. (2018) discuss the role of emotions in concept formation, especially
        # abstract concepts. Emotions play a vital role in how abstract concepts are understood
        # and recalled. Unlike AI, which lacks the capability to genuinely feel emotions,
        # human cognition is deeply intertwined with affective experiences. Emotions influence
        # the salience of specific concepts, enhance memory retention, and provide motivational
        # context, all of which are fundamental in abstract thinking and concept formation.
        emotions_dict = {
            "freedom": "A sense of joy, relief, and empowerment.",
            "knowledge": "Curiosity, satisfaction, and sometimes anxiety when challenged.",
            "love": "Warmth, attachment, vulnerability, and euphoria.",
            "fear": "Anxiety, heightened alertness, and desire to escape.",
            "success": "Pride, satisfaction, and motivation.",
            "failure": "Disappointment, frustration, and determination to improve.",
            "justice": "Righteousness, anger at injustice, and desire for fairness.",
            "creativity": "Excitement, flow, and occasional frustration.",
            "trust": "Security, comfort, and vulnerability.",
            "change": "Uncertainty, excitement, and fear of the unknown."
        }
        return emotions_dict.get(concept, "Emotional response not available for this concept.")

# Define AI Cognition Class
class AICognition:
    """
    A class to simulate AI concept acquisition using machine learning methodologies.
    This class models how AI systems use training data, model parameters, and reinforcement learning
    to acquire and form concepts.
    """
    def __init__(self, concept):
        # Cherkassky & Lee (2024) argue that AI concepts lack true abstraction and are mere
        # statistical mimicries AI systems, particularly large language models (LLMs), lack the
        # ability to genuinely abstract in the way that human cognition does. Their representations
        # are constructed through statistical correlations across vast datasets, leading to mimicry
        # rather than true understanding. Unlike humans, LLMs do not possess introspective or
        # situational grounding.
        self.concept = concept
        # LLMs rely on preprocessed training data, lacking situational and social grounding
        # (Borghi et al., 2018). The absence of social interaction and contextual understanding
        # means that LLMs operate in a vacuum, relying on syntactic regularities without the
        # benefit of pragmatic inference or embodied experiences.
        self.training_data = self.get_training_data(concept)
        self.model_parameters = {"layers": 12, "hidden_units": 768}
        # Fine-tuning relies on domain-specific data, unlike human conceptual evolution (Wei, 2020).
        # Unlike the developmental trajectory of human cognition, which evolves with increasing
        # complexity over time, LLMs undergo a process of fine-tuning on domain-specific data.
        # This adjustment is mechanical, involving parameter optimization without the cumulative,
        # adaptive, and self-directed learning seen in humans.
        self.fine_tuning_data = f"Domain-specific data related to '{concept}'"
        self.reinforcement_learning = "Reward-based learning mechanisms"

    def get_training_data(self, concept):
        """
        Retrieve training data used for AI to learn the concept.
        :param concept: str, the concept being acquired
        :return: str, description of training data related to the concept
        """
        # Cherkassky & Lee (2024) critique that LLMs generate knowledge based on statistical patterns.
        # AI's knowledge acquisition is limited by the constraints of statistical learning, where
        # concepts are inferred based on probabilistic patterns rather than causal relationships.
        # The data used by LLMs includes curated text sources, which provide only a surface-level
        # simulation of understanding, devoid of experiential or sensory grounding.
        training_data_dict = {
            "freedom": "Articles, social media posts, and speeches about freedom.",
            "knowledge": "Textbooks, research papers, and educational videos.",
            "love": "Books, poems, and movies related to love.",
            "fear": "Reports on phobias, horror movie scripts, and articles on dangers.",
            "success": "Case studies, biographies, and motivational content.",
            "failure": "Accounts of setbacks, failure analysis, and recovery strategies.",
            "justice": "Legal documents, case studies, and social justice literature.",
            "creativity": "Artworks, music, and stories about creative processes.",
            "trust": "Surveys on trust, psychological studies, and examples of trust-building.",
            "change": "Historical accounts, trend analysis, and articles on adaptability."
        }
        return training_data_dict.get(concept, "General training data for concept acquisition")

    def acquire_concept(self, category):
        """
        Simulate AI concept acquisition process based on a given category.
        Generate a concept map as a visual representation of the acquisition process.
        :param category: str, the category of concept acquisition (e.g., sensory processing,
                        context interpretation)
        :return: str, detailed explanation of the AI acquisition of the concept
        """
        # The `acquire_concept` method models the process by which AI systems acquire concepts by
        # categorizing the acquisition into different learning dimensions. Unlike human learning,
        # which involves flexible, context-driven interpretation, AI concept acquisition is primarily
        # mechanistic and relies on predefined data structures and learning algorithms. According to
        # Cherkassky & Lee (2024), AI systems such as large language models (LLMs) do not form true
        # conceptual representations; instead, they rely on recognizing statistical patterns within
        # large datasets. This leads to a form of 'concept acquisition' that is fundamentally devoid
        # of the introspective and dynamic contextual integration seen in human cognition
        # (Barsalou & Wiemer-Hastings, 2005).
        
        # Create a directed graph using NetworkX to represent the AI acquisition process
        G = nx.DiGraph()
        G.add_node(f"AI Acquisition of '{self.concept}'", size=1000)

        # Define nodes based on the selected category, which represents the specific aspect of
        # concept processing in AI. For example, in "sensory processing", AI uses image recognition
        # and text parsing to derive meaning, which does not have the same multimodal, dynamic sensory
        # integration as human sensory processing (Chiou & Ralph, 2019).
        if category == "sensory processing":
            # Sensory processing in AI is limited to predefined input channels, such as images
            # or text, which are processed independently without integrating multiple sensory
            # modalities in real-time. Chiou & Ralph (2019) argue that human semantic representation
            # is characterized by the dynamic interplay between hub (anterior temporal lobe) and
            # spoke (sensory-motor regions) components, which allows for multimodal integration.
            # By contrast, AI systems rely on isolated modalities that are processed without the
            # rich contextual interplay observed in human cognition.
            nodes = ["Image Recognition", "Audio Analysis", "Text Parsing"]
        elif category == "context interpretation":
            # Context interpretation for AI relies on identifying patterns in text, such as
            # sentiment analysis or contextual embeddings. Barsalou & Wiemer-Hastings (2005) highlight
            # that human abstract concepts are deeply grounded in situational variability and
            # introspective contexts, enabling flexible interpretation. AI's reliance on statistical
            # co-occurrences means it lacks true situational grounding, resulting in a superficial
            # level of context interpretation.
            nodes = ["Pattern Recognition", "Sentiment Analysis", "Contextual Understanding"]
        elif category == "memory retrieval":
            # Memory retrieval in AI involves accessing pre-trained models and knowledge graphs,
            # which provide static information based on past training. Carey (2011) discusses the
            # hierarchical nature of human concept acquisition, where new information is integrated
            # with existing knowledge in a dynamic manner. Unlike human memory, which is adaptive
            # and influenced by the emotional and contextual significance of experiences, AI memory
            # retrieval is limited to accessing stored representations without contextual reinterpretation.
            nodes = ["Knowledge Graphs", "Neural Network Weights", "Pre-trained Models"]
        elif category == "reinforcement learning":
            # Reinforcement learning for AI is based on trial and error and reward maximization, often
            # involving extrinsic reward signals. Marcus (2018) critiques this approach by emphasizing
            # that human learning is influenced by both intrinsic motivations and social contexts,
            # which are absent in AI systems. AI's reinforcement learning lacks the complex interplay
            # between intrinsic drives, social influences, and adaptive feedback that characterize
            # human learning.
            nodes = ["Trial and Error", "Reward Signal", "Policy Update"]
        elif category == "emotional integration":
            # Emotional integration for AI is simulated using sentiment analysis and user feedback,
            # but it lacks the genuine affective experience that humans possess. Borghi et al. (2018)
            # argue that emotions play a central role in human concept formation, especially for
            # abstract concepts. Human emotions are deeply intertwined with the process of abstraction,
            # influencing both the salience of concepts and their contextual relevance, whereas AI's
            # "emotions" are purely algorithmic and lack phenomenological depth.
            nodes = ["Sentiment Analysis", "Emotion Simulation", "User Feedback"]
        else:
            # For categories that do not fit predefined labels, AI processes involve generalized
            # data-driven techniques. The lack of flexibility in dynamically adapting to novel contexts,
            # a key feature of human cognitive flexibility (Lake et al., 2016), highlights the
            # limitations of current AI models in achieving true conceptual understanding.
            nodes = ["Data Processing", "Pattern Recognition", "Feature Extraction", "Generalization"]

        # Add nodes and edges to the graph
        for node in nodes:
            G.add_node(node, size=800)
            G.add_edge(f"AI Acquisition of '{self.concept}'", node)

        # Create a concept map as a visual representation of the AI concept acquisition process.
        # This representation highlights the sequential and hierarchical structure typical of AI
        # systems, in contrast to the dynamic, associative nature of human concept mapping. Laurence
        # & Margolis (2012) argue that human abstraction allows for the formation of general ideas
        # that go beyond sensory experiences, a capability that is limited in AI systems that rely
        # on predefined data patterns.
        plt.figure(figsize=(10, 8))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=[G.nodes[node].get('size', 800) for node in G],
            font_size=10, font_weight='bold')
        plt.title(f"Concept Map for AI Acquisition of '{self.concept}' - {category}")
        plt.show()
        print("The concept map has been generated and displayed.")

        # Provide additional details about the AI concept acquisition
        # The additional details highlight specific components of the AI acquisition process,
        # emphasizing the mechanical nature of training, fine-tuning, and reinforcement. Cherkassky
        # & Lee (2024) argue that such processes are limited to surface-level pattern recognition,
        # devoid of the introspective and situational depth that characterizes human concept formation.
        details = (
            f"Training Data: {self.training_data}\n"
            f"Model Parameters: {self.model_parameters}\n"
            f"Fine Tuning Data: {self.fine_tuning_data}\n"
            f"Reinforcement Learning: {self.reinforcement_learning}"
        )

        return (
            f"AI acquisition of '{self.concept}' in category '{category}':\n"
            "A concept map representing the key components has been generated.\n\n"
            f"Additional Details:\n{details}"
        )

# Chatbot function to explain concept acquisition
def chatbot_explanation(user_input, cognitive_system, category):
    """
    Provide a detailed explanation of concept acquisition for a given concept,
    cognitive system, and category.
    :param user_input: str, user-provided input indicating the concept to be explored
    :param cognitive_system: str, the cognitive system to be used ('human' or 'ai')
    :param category: str, the category of concept acquisition (e.g., sensory processing,
                    context interpretation)
    :return: str, detailed explanation of concept acquisition
    """
    concepts = [
        "freedom", "knowledge", "love", "fear", "success", "failure", "justice",
        "creativity", "trust", "change"
    ]
    categories = [
        "sensory processing", "context interpretation", "memory retrieval",
        "reinforcement learning", "emotional integration"
    ]

    if user_input.lower() == 'quit':
        return "Chat ended."

    if user_input.isdigit() and 1 <= int(user_input) <= len(concepts):
        concept = concepts[int(user_input) - 1]
    else:
        return "Invalid concept choice. Please choose a number between 1 and 10."

    if cognitive_system.lower() == 'human':
        # Human Cognition Explanation
        human = HumanCognition(concept)
        detailed_explanation = f"\n--- Human Concept Acquisition Process ---\n"
        detailed_explanation += f"Category: {category}\n"
        detailed_explanation += human.acquire_concept(category)
        return detailed_explanation

    elif cognitive_system.lower() == 'ai':
        # AI Cognition Explanation
        ai = AICognition(concept)
        detailed_explanation = f"\n--- AI Concept Acquisition Process ---\n"
        detailed_explanation += f"Category: {category}\n"
        detailed_explanation += ai.acquire_concept(category)
        closing_message = (
            "\nThe exploration of the concept is complete. "
            "Feel free to choose another concept to explore!"
            )
        return detailed_explanation + closing_message

    else:
        return "Invalid cognitive system. Please choose either 'human' or 'ai'."

# Main chat loop
if __name__ == "__main__":
    """
    Main loop for the chatbot, allowing users to interactively explore how humans and AI
    acquire and understand various concepts. Users can select concepts, choose between human
    or AI cognition, and explore different aspects of concept acquisition.
    """
    print("Welcome to the Human vs AI Concept Acquisition Chatbot!")
    print("Here, you can explore how humans and AI acquire and understand various concepts.")
    print(
    "You will be asked to provide a concept, choose a cognitive system (human or AI), "
    "and then explore specific categories of how that system forms a concept."
    )
    print("Type 'quit' to exit the chat.")
    while True:
        print("\nAvailable Concepts:")
        for i, concept in enumerate(["freedom", "knowledge", "love", "fear", "success",
            "failure", "justice", "creativity", "trust", "change"], start=1):
            print(f"{i}. {concept}")
        user_input = input("\nEnter the number of the concept you'd like to explore: ")
        if user_input.lower() == 'quit':
            print("\nChat ended by user.")
            break
        cognitive_system = input("\nWould you like to explore the concept acquisition by 'human' or 'ai'?: ")
        if cognitive_system.lower() not in ['human', 'ai']:
            print("Invalid choice. Please choose either 'human' or 'ai'.")
            continue
        while True:
            print("\nAvailable Categories:")
            for i, category in enumerate(["sensory processing", "context interpretation",
                "memory retrieval", "reinforcement learning", "emotional integration"], start=1):
                print(f"{i}. {category}")
            category_input = input("\nEnter the number of the category you'd like to focus on: ")
            if category_input.isdigit() and 1 <= int(category_input) <= 5:
                category = ["sensory processing", "context interpretation", "memory retrieval",
                "reinforcement learning", "emotional integration"][int(category_input) - 1]
            else:
                print("Invalid category choice. Please choose a number between 1 and 5.")
                continue
            explanation = chatbot_explanation(user_input, cognitive_system, category)
            print(explanation)
            while True:
                explore_more = input(
                    "\nWould you like to explore another aspect of this concept/category? "
                    "(1 for yes, 2 for no): "
                    )
                if explore_more in ['1', '2']:
                    break
                else:
                    print("Invalid input. Please enter 1 for yes or 2 for no.")
            if explore_more == '2':
                break
        if cognitive_system.lower() == 'human':
            while True:
                explore_ai = input("\nWould you like to explore the same concept by AI? (1 for yes, 2 for no): ")
                if explore_ai in ['1', '2']:
                    break
                else:
                    print("Invalid input. Please enter 1 for yes or 2 for no.")
            if explore_ai == '1':
                category_input = input("\nEnter the number of the category you'd like to focus on for AI: ")
                if category_input.isdigit() and 1 <= int(category_input) <= 5:
                    category = ["sensory processing", "context interpretation", "memory retrieval",
                    "reinforcement learning", "emotional integration"][int(category_input) - 1]
                    explanation = chatbot_explanation(user_input, 'ai', category)
                    print(explanation)
                continue
        elif cognitive_system.lower() == 'ai':
            while True:
                explore_human = input("\nWould you like to explore the same concept by Human? (1 for yes, 2 for no): ")
                if explore_human in ['1', '2']:
                    break
                else:
                    print("Invalid input. Please enter 1 for yes or 2 for no.")
            if explore_human == '1':
                category_input = input("\nEnter the number of the category you'd like to focus on for Human: ")
                if category_input.isdigit() and 1 <= int(category_input) <= 5:
                    category = ["sensory processing", "context interpretation", "memory retrieval",
                    "reinforcement learning", "emotional integration"][int(category_input) - 1]
                    explanation = chatbot_explanation(user_input, 'human', category)
                    print(explanation)
                continue
        while True:
            explore_another = input("\nWould you like to explore another concept? (1 for yes, 2 for no): ")
            if explore_another in ['1', '2']:
                break
            else:
                print("Invalid input. Please enter 1 for yes or 2 for no.")
        if explore_another == '2':
            print("\nChat ended by user.")
            break
