import hashlib

class SearchableEncryptionScheme:
    def __init__(self):
        self.forward_index = {}
        self.inverted_index = {}

    def encrypt(self, word):
        # 使用哈希函数对单词进行加密
        return hashlib.sha256(word.encode()).hexdigest()

    def generate_trapdoor(self, encrypted_word):
        # 使用哈希函数对密文单词进行陷门生成
        return hashlib.sha256(encrypted_word.encode()).hexdigest()

    def index_document(self, document):
        # 对文档进行加密和索引
        for word in document.split():
            encrypted_word = self.encrypt(word)
            trapdoor = self.generate_trapdoor(encrypted_word)

            if encrypted_word not in self.forward_index:
                self.forward_index[encrypted_word] = set()
            self.forward_index[encrypted_word].add(word)

            if trapdoor not in self.inverted_index:
                self.inverted_index[trapdoor] = set()
            self.inverted_index[trapdoor].add(encrypted_word)

    def search(self, query):
        # 对查询单词进行加密和陷门生成，并在倒排索引中查找对应的陷门
        encrypted_query = self.encrypt(query)
        trapdoor = self.generate_trapdoor(encrypted_query)

        if trapdoor in self.inverted_index:
            encrypted_results = self.inverted_index[trapdoor]
            results = set()
            for encrypted_word in encrypted_results:
                results.update(self.forward_index[encrypted_word])
            return results
        else:
            return set()

# 示例
scheme = SearchableEncryptionScheme()
document = "This is a sample document with some words"
scheme.index_document(document)

query = "sample"
results = scheme.search(query)
print(f"Results for query '{query}': {results}")