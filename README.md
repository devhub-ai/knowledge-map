# Knowledge-Map

**Knowledge-Map** is a Python package designed to convert unstructured data into a graph-based structure for enhanced visualization and analytics. By transforming raw data into meaningful knowledge graphs (KGs), this module enables more efficient query answering and business analytics, particularly when interfacing with large language models (LLMs).

## Problem Statement

Enterprise applications of Large Language Models (LLMs) hold promise for improving question answering capabilities on SQL databases. However, the full potential of LLMs in responding accurately to enterprise-specific questions remains untapped. This challenge is primarily due to the lack of appropriate benchmarks tailored to enterprise settings. Furthermore, current research indicates that LLMs can provide significantly more accurate answers when used in conjunction with Knowledge Graphs (KGs).

One relevant research study highlights that question-answering systems using GPT-4 achieve only a 16% accuracy rate when directly querying enterprise SQL databases using zero-shot prompts. However, by integrating Knowledge Graphs—representations that incorporate contextual and semantic business data—the accuracy can be raised to 54%.

### Research Paper Reference:

[A Benchmark to Understand the Role of Knowledge Graphs on Large Language Model's Accuracy for Question Answering on Enterprise SQL Databases](https://arxiv.org/abs/2311.07509)

This research demonstrates the value of using Knowledge Graphs for improving the accuracy of LLM-driven question answering systems, especially in enterprise contexts like insurance.

## Solution

**Knowledge-Map** addresses this problem by providing a systematic approach to convert unstructured data into a graph format, which can then be used to improve the performance of LLM-based question answering systems. 

The core idea is to avoid sending raw, unstructured data directly to an LLM for question answering. Instead, **Knowledge-Map** converts that data into a structured graph form that represents the relationships, hierarchies, and semantics in a clearer way, making it more useful for downstream analytics and machine learning models.

### How GraphQL Enhances the Solution

To further optimize data querying and response times, **Knowledge-Map** leverages **GraphQL** as an API structure. Unlike traditional REST APIs, which require multiple requests to fetch related data, GraphQL allows clients to specify exactly what data is needed in a single query, significantly reducing network bandwidth and improving response speed.

#### Key Advantages of Using GraphQL in Knowledge-Map:
1. **Reduced Network Bandwidth**: Clients can query exactly what they need, avoiding over-fetching or under-fetching of data.
2. **Faster Response Times**: Single, efficient queries reduce the need for multiple API calls, leading to faster responses.
3. **Flexibility**: The API can evolve without versioning as GraphQL offers more flexible query patterns, ensuring that the application remains future-proof.
4. **Optimized for Graph-Based Data**: GraphQL's structure is ideal for querying knowledge graphs, as it allows for complex relationships to be navigated in a single request.

<!-- ## How Knowledge-Map Works
1. **Data Ingestion**: Knowledge-Map ingests unstructured datasets, whether text-based or semi-structured formats.
2. **Graph Construction**: The unstructured data is transformed into a knowledge graph, which captures the relationships between different entities.
3. **Query Interface (Powered by GraphQL)**: The graph can be queried using LLMs (e.g., GPT-4) via GraphQL APIs, improving the accuracy and efficiency of responses.
4. **Visualization and Analytics**: The graph-based structure enables powerful visualization capabilities, helping businesses understand the context and connections within their data. -->

<!-- ## Installation

To install the package, simply use pip:

```bash
pip install knowledge-map
```

## Usage

```python
from knowledge_map import KnowledgeMap

# Initialize the KnowledgeMap
km = KnowledgeMap()

# Ingest your unstructured data
data = "Your raw unstructured data here"
km.ingest_data(data)

# Convert to a graph
graph = km.build_graph()

# Visualize or query the graph using GraphQL
km.visualize_graph()

# Example GraphQL query
query = """
{
  entity(name: "customer") {
    id
    name
    relatedEntities {
      name
    }
  }
}
"""
result = km.query_graph(query)
``` -->

## Key Features

- **Unstructured to Structured Conversion**: Seamlessly transform unstructured data into a knowledge graph.
- **GraphQL Integration**: Utilize GraphQL to efficiently query and interact with the knowledge graph, reducing network bandwidth and improving response time.
- **Improved LLM Querying**: Leverage the power of KGs to improve the accuracy of question-answering systems.
- **Visualization**: Enhanced analytics through clear graph-based visualization of data relationships.
- **Enterprise-Ready**: Designed for enterprise applications with large-scale, complex datasets.

## Applications
- Enterprise database querying (e.g., SQL databases in industries like insurance or finance)
- Business intelligence and reporting
- Enhancing LLM-powered applications with contextual knowledge

## Contributing

We welcome contributions from the community. Feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the [MIT](LICENSE) License.

