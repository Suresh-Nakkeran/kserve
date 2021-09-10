/*

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// Code generated by client-gen. DO NOT EDIT.

package fake

import (
	v1beta1 "github.com/kserve/kserve/pkg/apis/serving/v1beta1"
	v1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	labels "k8s.io/apimachinery/pkg/labels"
	schema "k8s.io/apimachinery/pkg/runtime/schema"
	types "k8s.io/apimachinery/pkg/types"
	watch "k8s.io/apimachinery/pkg/watch"
	testing "k8s.io/client-go/testing"
)

// FakeInferenceServices implements InferenceServiceInterface
type FakeInferenceServices struct {
	Fake *FakeServingV1beta1
	ns   string
}

var inferenceservicesResource = schema.GroupVersionResource{Group: "serving", Version: "v1beta1", Resource: "inferenceservices"}

var inferenceservicesKind = schema.GroupVersionKind{Group: "serving", Version: "v1beta1", Kind: "InferenceService"}

// Get takes name of the inferenceService, and returns the corresponding inferenceService object, and an error if there is any.
func (c *FakeInferenceServices) Get(name string, options v1.GetOptions) (result *v1beta1.InferenceService, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewGetAction(inferenceservicesResource, c.ns, name), &v1beta1.InferenceService{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1beta1.InferenceService), err
}

// List takes label and field selectors, and returns the list of InferenceServices that match those selectors.
func (c *FakeInferenceServices) List(opts v1.ListOptions) (result *v1beta1.InferenceServiceList, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewListAction(inferenceservicesResource, inferenceservicesKind, c.ns, opts), &v1beta1.InferenceServiceList{})

	if obj == nil {
		return nil, err
	}

	label, _, _ := testing.ExtractFromListOptions(opts)
	if label == nil {
		label = labels.Everything()
	}
	list := &v1beta1.InferenceServiceList{ListMeta: obj.(*v1beta1.InferenceServiceList).ListMeta}
	for _, item := range obj.(*v1beta1.InferenceServiceList).Items {
		if label.Matches(labels.Set(item.Labels)) {
			list.Items = append(list.Items, item)
		}
	}
	return list, err
}

// Watch returns a watch.Interface that watches the requested inferenceServices.
func (c *FakeInferenceServices) Watch(opts v1.ListOptions) (watch.Interface, error) {
	return c.Fake.
		InvokesWatch(testing.NewWatchAction(inferenceservicesResource, c.ns, opts))

}

// Create takes the representation of a inferenceService and creates it.  Returns the server's representation of the inferenceService, and an error, if there is any.
func (c *FakeInferenceServices) Create(inferenceService *v1beta1.InferenceService) (result *v1beta1.InferenceService, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewCreateAction(inferenceservicesResource, c.ns, inferenceService), &v1beta1.InferenceService{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1beta1.InferenceService), err
}

// Update takes the representation of a inferenceService and updates it. Returns the server's representation of the inferenceService, and an error, if there is any.
func (c *FakeInferenceServices) Update(inferenceService *v1beta1.InferenceService) (result *v1beta1.InferenceService, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewUpdateAction(inferenceservicesResource, c.ns, inferenceService), &v1beta1.InferenceService{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1beta1.InferenceService), err
}

// UpdateStatus was generated because the type contains a Status member.
// Add a +genclient:noStatus comment above the type to avoid generating UpdateStatus().
func (c *FakeInferenceServices) UpdateStatus(inferenceService *v1beta1.InferenceService) (*v1beta1.InferenceService, error) {
	obj, err := c.Fake.
		Invokes(testing.NewUpdateSubresourceAction(inferenceservicesResource, "status", c.ns, inferenceService), &v1beta1.InferenceService{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1beta1.InferenceService), err
}

// Delete takes name of the inferenceService and deletes it. Returns an error if one occurs.
func (c *FakeInferenceServices) Delete(name string, options *v1.DeleteOptions) error {
	_, err := c.Fake.
		Invokes(testing.NewDeleteAction(inferenceservicesResource, c.ns, name), &v1beta1.InferenceService{})

	return err
}

// DeleteCollection deletes a collection of objects.
func (c *FakeInferenceServices) DeleteCollection(options *v1.DeleteOptions, listOptions v1.ListOptions) error {
	action := testing.NewDeleteCollectionAction(inferenceservicesResource, c.ns, listOptions)

	_, err := c.Fake.Invokes(action, &v1beta1.InferenceServiceList{})
	return err
}

// Patch applies the patch and returns the patched inferenceService.
func (c *FakeInferenceServices) Patch(name string, pt types.PatchType, data []byte, subresources ...string) (result *v1beta1.InferenceService, err error) {
	obj, err := c.Fake.
		Invokes(testing.NewPatchSubresourceAction(inferenceservicesResource, c.ns, name, pt, data, subresources...), &v1beta1.InferenceService{})

	if obj == nil {
		return nil, err
	}
	return obj.(*v1beta1.InferenceService), err
}
